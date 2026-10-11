"""
Render the GIFT-format knowledge check .txt into a reviewable PDF.

Usage:
    python build_pdf.py <input.txt> <output.pdf>

If args are omitted, defaults to the sibling .txt / .pdf with today's date pattern.
"""
import re
import sys
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageBreak, PageTemplate, Paragraph,
    Spacer, Table, TableStyle, KeepTogether, HRFlowable,
)


QUESTION_BLOCK_RE = re.compile(
    r"// question:\s*(\d+)\s*\n"
    r"::::\[choice\]<p>(.*?)</p>\{\s*\n"
    r"(.*?)\n\}",
    re.DOTALL,
)
OPTION_RE = re.compile(r"\s*([=~])%(-?\d+)%<p>(.*?)</p>#\s*")


def unescape_gift(text: str) -> str:
    """Unescape GIFT special characters back to readable text."""
    return text.replace(r"\:", ":").replace("&amp;", "&")


def parse_gift(text: str):
    """Yield (qnum, qtext, [(is_correct, opt_text), ...]) tuples."""
    for match in QUESTION_BLOCK_RE.finditer(text):
        qnum = match.group(1)
        qtext = unescape_gift(match.group(2))
        options_block = match.group(3)
        options = []
        for line in options_block.splitlines():
            m = OPTION_RE.match(line)
            if not m:
                continue
            mark, percent_str, opt_text = m.group(1), m.group(2), unescape_gift(m.group(3))
            # Single-correct: =%1000%. Multi-select: ~%POSITIVE% correct, ~%-N%/~%0% wrong.
            is_correct = mark == "=" or (mark == "~" and int(percent_str) > 0)
            options.append((is_correct, opt_text))
        yield qnum, qtext, options


def classify(qtext: str, options: list) -> str:
    """Tag a question as T/F, single-MC, or multi-select."""
    if len(options) == 2 and {o[1] for o in options} == {"True", "False"}:
        return "True / False"
    n_correct = sum(1 for c, _ in options if c)
    if n_correct > 1:
        return "Multiple Choice  •  Select multiple"
    return "Multiple Choice"


# ---------- PDF rendering ----------

styles = getSampleStyleSheet()

H_TITLE = ParagraphStyle(
    "kc_title", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=28, leading=34, textColor=colors.HexColor("#1e3a5f"),
    spaceAfter=8, alignment=1,
)
H_SUB = ParagraphStyle(
    "kc_sub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=14, leading=20, textColor=colors.HexColor("#5b6470"),
    alignment=1, spaceAfter=4,
)
H_TAG = ParagraphStyle(
    "kc_tag", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=8, leading=10, textColor=colors.white,
    backColor=colors.HexColor("#1e3a5f"),
    borderPadding=(3, 6, 3, 6), spaceAfter=4,
)
H_QNUM = ParagraphStyle(
    "kc_qnum", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=9, leading=11, textColor=colors.HexColor("#94a3b8"),
    spaceAfter=2,
)
H_Q = ParagraphStyle(
    "kc_q", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=11.5, leading=15, textColor=colors.HexColor("#0f172a"),
    spaceAfter=8,
)
H_OPT = ParagraphStyle(
    "kc_opt", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10.5, leading=14, textColor=colors.HexColor("#334155"),
    leftIndent=22, firstLineIndent=-18, spaceAfter=3,
)
H_OPT_OK = ParagraphStyle(
    "kc_opt_ok", parent=H_OPT, fontName="Helvetica-Bold",
    textColor=colors.HexColor("#15803d"),
)
H_SECTION = ParagraphStyle(
    "kc_section", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=16, leading=20, textColor=colors.HexColor("#1e3a5f"),
    spaceBefore=12, spaceAfter=8,
)
H_BODY = ParagraphStyle(
    "kc_body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=11, leading=15, textColor=colors.HexColor("#334155"),
    spaceAfter=6,
)


def make_page_decoration(total_questions: int):
    """Header brand bar + footer page number, with header question-count
    closed over the actual count parsed from the bank."""
    def _page_decoration(canvas_obj, doc):
        canvas_obj.saveState()
        width, height = LETTER
        # Top brand strip
        canvas_obj.setFillColor(colors.HexColor("#1e3a5f"))
        canvas_obj.rect(0, height - 0.35 * inch, width, 0.35 * inch, fill=1, stroke=0)
        canvas_obj.setFillColor(colors.white)
        canvas_obj.setFont("Helvetica-Bold", 10)
        canvas_obj.drawString(0.5 * inch, height - 0.23 * inch, "RPM Apps Workshop  •  Knowledge Check")
        canvas_obj.setFont("Helvetica", 9)
        canvas_obj.drawRightString(width - 0.5 * inch, height - 0.23 * inch, f"{total_questions} questions  •  Materials-allowed")
        # Footer page number
        canvas_obj.setFillColor(colors.HexColor("#94a3b8"))
        canvas_obj.setFont("Helvetica", 9)
        canvas_obj.drawRightString(width - 0.5 * inch, 0.4 * inch, f"Page {doc.page}")
        canvas_obj.drawString(0.5 * inch, 0.4 * inch, "RPM Knowledge Check  •  2026-06-17")
        canvas_obj.restoreState()
    return _page_decoration


def render(input_path: Path, output_path: Path):
    questions = list(parse_gift(input_path.read_text(encoding="utf-8")))

    doc = BaseDocTemplate(
        str(output_path), pagesize=LETTER,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        topMargin=0.7 * inch, bottomMargin=0.6 * inch,
        title="RPM Apps Workshop — Knowledge Check",
        author="RPM Apps Workshop",
    )
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="kc", frames=[frame], onPage=make_page_decoration(len(questions)))])

    story = []

    # Cover
    story.append(Spacer(1, 1.4 * inch))
    story.append(Paragraph("RPM Apps Workshop", H_TITLE))
    story.append(Paragraph("Knowledge Check", H_TITLE))
    story.append(Spacer(1, 0.3 * inch))
    n_tf = sum(1 for _, qt, opts in questions if classify(qt, opts) == "True / False")
    n_mc = len(questions) - n_tf
    story.append(Paragraph(f"{len(questions)} questions &middot; {n_tf} True/False &middot; {n_mc} multiple choice", H_SUB))
    story.append(Paragraph("Difficulty target: 5 / 10  &middot;  materials-allowed", H_SUB))
    story.append(Paragraph("Delivery: 10 random questions per attempt  &middot;  pass = 8 of 10", H_SUB))
    story.append(Spacer(1, 0.4 * inch))

    # Section definitions: (label, qnum_lo, qnum_hi)
    SECTIONS = [
        ("Suite / TAWA / Application Framework", 3001, 3017),
        ("Territory & Quota",                    3018, 3051),
        ("Account Segmentation & Scoring",       3052, 3072),
        ("Go-to-Market Capacity Planning",       3073, 3093),
        ("Sales Forecasting (incl. AI Prediction Lab)", 3094, 3107),
        ("Cross-app & Reference",                3108, 3119),
    ]
    # Count actual questions per section from the parsed bank (handles deletions)
    qnums = [int(qnum) for qnum, _qt, _opts in questions]
    summary = [["Section", "Range", "Questions"]]
    for label, lo, hi in SECTIONS:
        count = sum(1 for n in qnums if lo <= n <= hi)
        summary.append([label, f"{lo}–{hi}", str(count)])
    tbl = Table(summary, colWidths=[3.6 * inch, 1.4 * inch, 1.0 * inch], hAlign="CENTER")
    tbl.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e3a5f")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f1f5f9")]),
        ("LINEBELOW", (0, 0), (-1, 0), 1, colors.HexColor("#0f172a")),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(tbl)

    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph(
        "<font color='#5b6470'>Correct answers are <b><font color='#15803d'>highlighted in green with a checkmark</font></b>. "
        "True/False questions show 2 options; multiple-choice questions show 4. Wrong distractors are intentionally "
        "close-to-correct to test understanding rather than guessing.</font>", H_BODY,
    ))

    story.append(PageBreak())

    # Section anchors for question ranges (printed before the first question in each range)
    section_starts = {
        "3001": "Suite / TAWA / Application Framework",
        "3016": "Territory & Quota",
        "3033": "Account Segmentation & Scoring",
        "3045": "Go-to-Market Capacity Planning",
        "3060": "Sales Forecasting (incl. AI Prediction Lab)",
        "3092": "Cross-app & Reference",
    }

    for qnum, qtext, options in questions:
        block = []
        if qnum in section_starts:
            block.append(Paragraph(section_starts[qnum], H_SECTION))

        kind = classify(qtext, options)
        block.append(Paragraph(f"Q{qnum} &middot; {kind}", H_QNUM))
        block.append(Paragraph(escape(qtext), H_Q))

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, (is_correct, opt_text) in enumerate(options):
            letter = letters[i] if len(options) > 2 else ("T" if opt_text == "True" else "F")
            # ZapfDingbats character "4" is a heavy check mark — guaranteed to render
            marker = (
                '<font name="ZapfDingbats" color="#15803d" size="11">4</font>'
                if is_correct else '<font color="#cbd5e1">&#9675;</font>'
            )
            # Use ZapfDingbats hollow circle (open dot, U+25CB) as the not-correct marker via the same font:
            if not is_correct:
                marker = '<font color="#cbd5e1" size="11">o</font>'
            style = H_OPT_OK if is_correct else H_OPT
            block.append(Paragraph(f"<b>{letter}.</b>&nbsp; {marker}&nbsp;&nbsp;{escape(opt_text)}", style))

        # Soft divider — colored horizontal rule
        block.append(Spacer(1, 4))
        block.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#e2e8f0"), spaceBefore=0, spaceAfter=8))

        story.append(KeepTogether(block))

    doc.build(story)
    print(f"Wrote {output_path}  ({output_path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    here = Path(__file__).parent
    if len(sys.argv) >= 3:
        in_path = Path(sys.argv[1])
        out_path = Path(sys.argv[2])
    else:
        in_path = here / "RPM Knowledge Check_export_2026-06-17.txt"
        out_path = here / "RPM Knowledge Check_2026-06-17.pdf"
    render(in_path, out_path)
