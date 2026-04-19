#!/usr/bin/env python3
"""Quick heuristic audit for academic Beamer slide decks.

This tool is intentionally lightweight. It is meant to catch obvious layout
risks early:
- too many bullets or major blocks
- figures that are too wide or too small
- imbalanced side-by-side columns
- overfull / underfull warnings in the LaTeX log

It does not replace a visual review of the PDF, but it is a fast first pass.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


FRAME_BEGIN_RE = re.compile(r"\\begin\{frame\}(?:\[[^\]]*\])?(?:\{(?P<title>[^}]*)\})?")
FRAMETITLE_RE = re.compile(r"\\frametitle\{(?P<title>[^}]*)\}")
ITEM_RE = re.compile(r"\\item\b")
INCLUDEGRAPHICS_RE = re.compile(r"\\includegraphics(?:\[(?P<opts>[^\]]*)\])?\{(?P<path>[^}]*)\}")
COLUMN_RE = re.compile(r"\\column\{(?P<width>[^}]*)\}")
WIDTH_RE = re.compile(r"width\s*=\s*(?P<num>[0-9]*\.?[0-9]+)?\s*\\(?P<unit>linewidth|textwidth|paperwidth)")
FIGURE_ENV_RE = re.compile(r"\\begin\{figure\}")
TABLE_ENV_RE = re.compile(r"\\begin\{table\}")
COLUMNS_ENV_RE = re.compile(r"\\begin\{columns\}")
ITEMIZE_ENV_RE = re.compile(r"\\begin\{itemize\}")
ENUMERATE_ENV_RE = re.compile(r"\\begin\{enumerate\}")
BLOCK_ENV_RE = re.compile(r"\\begin\{block\}")
MINIPAGE_ENV_RE = re.compile(r"\\begin\{minipage\}")
EQUATION_ENV_RE = re.compile(r"\\begin\{equation\*?\}")
ALIGN_ENV_RE = re.compile(r"\\begin\{align\*?\}")
GATHER_ENV_RE = re.compile(r"\\begin\{gather\*?\}")

LOG_WARNING_RE = re.compile(
    r"(?P<kind>Overfull|Underfull)\s+\\(?P<axis>[hv])box.*?(?:at lines?\s+(?P<start>\d+)(?:--(?P<end>\d+))?)?",
    re.IGNORECASE,
)


@dataclass
class FrameAudit:
    index: int
    start_line: int
    end_line: int
    title: str
    lines: list[str] = field(default_factory=list)
    items: int = 0
    includegraphics_count: int = 0
    figure_widths: list[Optional[float]] = field(default_factory=list)
    column_widths: list[Optional[float]] = field(default_factory=list)
    major_blocks: int = 0
    text_lines: int = 0
    log_warnings: list[str] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)


def strip_comments(line: str) -> str:
    return re.sub(r"(?<!\\)%.*$", "", line)


def extract_frame_title(begin_line: str) -> str:
    match = FRAME_BEGIN_RE.search(begin_line)
    if match:
        title = (match.group("title") or "").strip()
        if title:
            return title
    return ""


def parse_width_value(spec: str) -> Optional[float]:
    spec = spec.strip()
    if not spec:
        return None

    match = WIDTH_RE.search(spec)
    if match:
        num = match.group("num")
        return float(num) if num else 1.0

    if re.search(r"\\(linewidth|textwidth|paperwidth)\b", spec):
        return 1.0

    return None


def classify_title(title: str, frame_text: str) -> bool:
    text = f"{title} {frame_text}".lower()
    if "\\titlepage" in text or "\\tableofcontents" in text:
        return True
    exempt_terms = (
        "agenda",
        "outline",
        "contents",
        "toc",
        "references",
        "reference",
        "q&a",
        "questions",
        "thanks",
        "appendix",
    )
    return any(term in text for term in exempt_terms)


def split_frames(lines: list[str]) -> list[FrameAudit]:
    frames: list[FrameAudit] = []
    current: Optional[FrameAudit] = None

    for lineno, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")
        if "\\begin{frame}" in line:
            current = FrameAudit(
                index=len(frames) + 1,
                start_line=lineno,
                end_line=lineno,
                title=extract_frame_title(line),
                lines=[line],
            )
            if "\\end{frame}" in line:
                frames.append(current)
                current = None
            continue

        if current is None:
            continue

        current.lines.append(line)
        current.end_line = lineno
        if "\\end{frame}" in line:
            frames.append(current)
            current = None

    return frames


def analyze_frame(frame: FrameAudit, args: argparse.Namespace) -> None:
    clean_lines = [strip_comments(line) for line in frame.lines]
    block_text = "\n".join(clean_lines)

    if not frame.title:
        match = FRAMETITLE_RE.search(block_text)
        if match:
            frame.title = match.group("title").strip()
    if not frame.title:
        frame.title = f"frame-{frame.index}"

    frame.items = len(ITEM_RE.findall(block_text))
    frame.includegraphics_count = len(INCLUDEGRAPHICS_RE.findall(block_text))

    frame.figure_widths = []
    for match in INCLUDEGRAPHICS_RE.finditer(block_text):
        opts = match.group("opts") or ""
        frame.figure_widths.append(parse_width_value(opts))

    frame.column_widths = []
    for match in COLUMN_RE.finditer(block_text):
        frame.column_widths.append(parse_width_value(match.group("width")))

    major_block_patterns = (
        FIGURE_ENV_RE,
        TABLE_ENV_RE,
        COLUMNS_ENV_RE,
        ITEMIZE_ENV_RE,
        ENUMERATE_ENV_RE,
        BLOCK_ENV_RE,
        MINIPAGE_ENV_RE,
        EQUATION_ENV_RE,
        ALIGN_ENV_RE,
        GATHER_ENV_RE,
    )
    frame.major_blocks = sum(len(pattern.findall(block_text)) for pattern in major_block_patterns)

    frame.text_lines = 0
    for raw_line in clean_lines:
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("\\begin{frame}") or stripped.startswith("\\end{frame}"):
            continue
        if stripped.startswith("\\begin{") or stripped.startswith("\\end{"):
            continue
        if stripped.startswith("\\includegraphics"):
            continue
        if stripped.startswith("\\centering") or stripped.startswith("\\vspace") or stripped.startswith("\\hspace"):
            continue
        if re.search(r"[A-Za-z0-9\u4e00-\u9fff]", stripped):
            frame.text_lines += 1

    is_exempt = classify_title(frame.title, block_text)

    if not is_exempt:
        if frame.includegraphics_count == 0:
            frame.issues.append("no visual anchor")
        if frame.items > args.max_bullets:
            frame.issues.append(f"{frame.items} bullets (target <= {args.max_bullets})")
        if frame.major_blocks > args.max_major_blocks:
            frame.issues.append(f"{frame.major_blocks} major blocks (target <= {args.max_major_blocks})")
        if frame.text_lines > args.max_text_lines:
            frame.issues.append(f"{frame.text_lines} text-heavy lines (target <= {args.max_text_lines})")

    if not is_exempt:
        if frame.includegraphics_count > args.max_figures:
            frame.issues.append(f"{frame.includegraphics_count} figures (target <= {args.max_figures})")

        for width in frame.figure_widths:
            if width is None:
                continue
            if width > args.max_figure_width:
                frame.issues.append(f"figure width {width:.2f}\\linewidth is too large")
            elif width < args.min_figure_width:
                frame.issues.append(f"figure width {width:.2f}\\linewidth is likely too small")

        known_column_widths = [width for width in frame.column_widths if width is not None]
        if len(known_column_widths) >= 2:
            widest = max(known_column_widths)
            narrowest = min(known_column_widths)
            if widest - narrowest > args.max_column_imbalance:
                frame.issues.append(
                    f"column imbalance {widest:.2f}/{narrowest:.2f} exceeds {args.max_column_imbalance:.2f}"
                )


def scan_log(log_path: Path) -> list[tuple[str, Optional[int], Optional[int]]]:
    if not log_path.exists():
        return []

    warnings: list[tuple[str, Optional[int], Optional[int]]] = []
    for raw_line in log_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = LOG_WARNING_RE.search(raw_line)
        if not match:
            continue
        kind = f"{match.group('kind')} \\{match.group('axis')}box"
        start = match.group("start")
        end = match.group("end")
        warnings.append((kind, int(start) if start else None, int(end) if end else None))
    return warnings


def attach_log_warnings(frames: list[FrameAudit], warnings: list[tuple[str, Optional[int], Optional[int]]]) -> list[str]:
    global_warnings: list[str] = []
    for kind, start, end in warnings:
        if start is None:
            global_warnings.append(kind)
            continue

        end_line = end or start
        matched = False
        for frame in frames:
            if frame.start_line <= end_line and frame.end_line >= start:
                frame.log_warnings.append(f"{kind} at lines {start}--{end_line}")
                matched = True
        if not matched:
            global_warnings.append(f"{kind} at lines {start}--{end_line}")
    return global_warnings


def render_frame_report(frame: FrameAudit) -> str:
    status = "OK" if not frame.issues and not frame.log_warnings else "WARN"
    lines = [
        f"[Frame {frame.index}] {frame.title} (lines {frame.start_line}-{frame.end_line}) => {status}",
    ]
    for item in frame.issues:
        lines.append(f"  - {item}")
    for warning in frame.log_warnings:
        lines.append(f"  - log: {warning}")
    if not frame.issues and not frame.log_warnings:
        lines.append("  - no obvious layout issues detected")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Heuristic audit for Beamer slide layout and density.")
    parser.add_argument("--tex", required=True, help="Path to the main .tex file")
    parser.add_argument("--log", default="", help="Optional path to the .log file")
    parser.add_argument("--max-bullets", type=int, default=4)
    parser.add_argument("--max-major-blocks", type=int, default=3)
    parser.add_argument("--max-figures", type=int, default=2)
    parser.add_argument("--min-figure-width", type=float, default=0.35)
    parser.add_argument("--max-figure-width", type=float, default=0.85)
    parser.add_argument("--max-column-imbalance", type=float, default=0.20)
    parser.add_argument("--max-text-lines", type=int, default=10)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    tex_path = Path(args.tex).expanduser().resolve()
    if not tex_path.exists():
        raise FileNotFoundError(tex_path)

    lines = tex_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    frames = split_frames(lines)
    if not frames:
        print(f"source={tex_path}")
        print("frames_found=0")
        print("No frame environments found.")
        return 0

    for frame in frames:
        analyze_frame(frame, args)

    global_warnings: list[str] = []
    if args.log:
        log_path = Path(args.log).expanduser().resolve()
        global_warnings = attach_log_warnings(frames, scan_log(log_path))

    warn_frames = [frame for frame in frames if frame.issues or frame.log_warnings]

    print(f"source={tex_path}")
    if args.log:
        print(f"log={Path(args.log).expanduser().resolve()}")
    print(f"frames_found={len(frames)}")
    print(f"frames_with_warnings={len(warn_frames)}")
    if global_warnings:
        print("global_warnings:")
        for warning in global_warnings:
            print(f"  - {warning}")

    for frame in frames:
        print(render_frame_report(frame))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
