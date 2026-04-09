import argparse
from pathlib import Path

import fitz


def parse_pages(pages_text: str, total_pages: int) -> list[int]:
    pages = set()
    for part in pages_text.split(","):
        token = part.strip()
        if not token:
            continue
        if "-" in token:
            left, right = token.split("-", 1)
            start = max(1, int(left))
            end = min(total_pages, int(right))
            if start <= end:
                for p in range(start, end + 1):
                    pages.add(p - 1)
        else:
            p = int(token)
            if 1 <= p <= total_pages:
                pages.add(p - 1)
    return sorted(pages)


def extract_embedded_images(doc: fitz.Document, out_dir: Path, min_width: int, min_height: int) -> int:
    seen_xrefs = set()
    saved = 0
    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        images = page.get_images(full=True)
        image_idx = 0
        for image in images:
            xref = image[0]
            if xref in seen_xrefs:
                continue
            pix = fitz.Pixmap(doc, xref)
            if pix.width < min_width or pix.height < min_height:
                continue
            if pix.n > 4:
                pix = fitz.Pixmap(fitz.csRGB, pix)
            image_idx += 1
            output_path = out_dir / f"page_{page_index + 1:03d}_img_{image_idx:02d}.png"
            pix.save(output_path.as_posix())
            seen_xrefs.add(xref)
            saved += 1
    return saved


def extract_image_blocks(doc: fitz.Document, out_dir: Path, min_width: int, min_height: int, dpi: int) -> int:
    saved = 0
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        page_dict = page.get_text("dict")
        block_idx = 0
        for block in page_dict.get("blocks", []):
            if block.get("type") != 1:
                continue
            x0, y0, x1, y1 = block.get("bbox")
            if (x1 - x0) < min_width or (y1 - y0) < min_height:
                continue
            clip = fitz.Rect(x0, y0, x1, y1)
            pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
            block_idx += 1
            output_path = out_dir / f"page_{page_index + 1:03d}_block_{block_idx:02d}.png"
            pix.save(output_path.as_posix())
            saved += 1
    return saved


def extract_caption_regions(doc: fitz.Document, out_dir: Path, dpi: int, min_height: int) -> int:
    saved = 0
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        page_w = page.rect.width
        page_h = page.rect.height
        blocks = page.get_text("blocks")
        captions = []
        for b in blocks:
            x0, y0, x1, y1, text = b[0], b[1], b[2], b[3], b[4]
            t = (text or "").strip().lower()
            if t.startswith("figure ") or t.startswith("fig."):
                col = 0 if (x0 + x1) * 0.5 < page_w * 0.5 else 1
                captions.append((x0, y0, x1, y1, col))
        captions.sort(key=lambda v: (v[4], v[1]))
        by_col = {0: [], 1: []}
        for c in captions:
            by_col[c[4]].append(c)
        for col in [0, 1]:
            col_caps = by_col[col]
            for idx, cap in enumerate(col_caps):
                _, y0, _, _, _ = cap
                prev_y1 = 55.0
                if idx > 0:
                    prev_y1 = col_caps[idx - 1][3] + 8.0
                cap_top = max(prev_y1, y0 - 320.0)
                cap_bottom = max(prev_y1 + 20.0, y0 - 6.0)
                if (cap_bottom - cap_top) < min_height:
                    continue
                if col == 0:
                    clip = fitz.Rect(25.0, cap_top, page_w * 0.5 - 10.0, cap_bottom)
                else:
                    clip = fitz.Rect(page_w * 0.5 + 10.0, cap_top, page_w - 25.0, cap_bottom)
                clip = clip & page.rect
                if clip.height < min_height or clip.width < 120:
                    continue
                pix = page.get_pixmap(matrix=matrix, clip=clip, alpha=False)
                output_path = out_dir / f"page_{page_index + 1:03d}_figcap_{saved + 1:02d}.png"
                pix.save(output_path.as_posix())
                saved += 1
    return saved


def render_pages(doc: fitz.Document, out_dir: Path, page_indices: list[int], dpi: int) -> int:
    if not page_indices:
        return 0
    saved = 0
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    for page_index in page_indices:
        page = doc.load_page(page_index)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        output_path = out_dir / f"page_{page_index + 1:03d}_full.png"
        pix.save(output_path.as_posix())
        saved += 1
    return saved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--min-width", type=int, default=300)
    parser.add_argument("--min-height", type=int, default=180)
    parser.add_argument("--render-pages", default="")
    parser.add_argument("--dpi", type=int, default=220)
    parser.add_argument("--extract-blocks", action="store_true")
    parser.add_argument("--extract-captions", action="store_true")
    args = parser.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path.as_posix())
    embedded_saved = extract_embedded_images(doc, out_dir, args.min_width, args.min_height)
    block_saved = 0
    caption_saved = 0
    if args.extract_blocks:
        block_saved = extract_image_blocks(doc, out_dir, args.min_width, args.min_height, args.dpi)
    if args.extract_captions:
        caption_saved = extract_caption_regions(doc, out_dir, args.dpi, args.min_height)

    page_indices = []
    if args.render_pages.strip():
        page_indices = parse_pages(args.render_pages, doc.page_count)
    pages_saved = render_pages(doc, out_dir, page_indices, args.dpi)

    print(f"pdf={pdf_path}")
    print(f"out={out_dir}")
    print(f"embedded_images_saved={embedded_saved}")
    print(f"image_blocks_saved={block_saved}")
    print(f"caption_regions_saved={caption_saved}")
    print(f"rendered_pages_saved={pages_saved}")


if __name__ == "__main__":
    main()
