#!/usr/bin/env python3
"""Tata Motors diploma report — full research text + student PDF images, aligned layout."""

from __future__ import annotations

import zipfile
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
import subprocess

from report_content import (
    ABOUT,
    ACHIEVEMENTS_FY25,
    CHALLENGES,
    CHALLENGES_INTRO,
    CONCLUSION,
    ECE,
    ECE_BULLETS,
    EXECUTIVE_SUMMARY,
    HISTORY,
    INTERNSHIP_PROGRAMMES,
    INTRO,
    METHODOLOGY,
    METHODOLOGY_BULLETS,
    MFG_INTRO,
    MFG_SECTIONS,
    OVERVIEW,
    PLANTS,
    PRODUCT_BLOCKS,
    PRODUCT_TABLE,
    PRODUCTS_INTRO,
    RD_INNOVATION,
    REFERENCES,
    SEGMENT_CV,
    SEGMENT_CV_TEXT,
    SEGMENT_EV,
    SEGMENT_EV_TEXT,
    SEGMENT_JLR,
    SEGMENT_PV,
    SEGMENT_PV_TEXT,
    STRENGTHS,
    SUSTAINABILITY,
)

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
OUT = ROOT / "output"
STUDENT = {
    "name": "Nachiket L Karoshi",
    "department": "Diploma in Electronics and Communication Engineering",
    "institution": "KLE Society's C B Kolli Polytechnic, Haveri",
    "internship_org": "Tata Motors Limited",
    "academic_year": "2026–2027",
    "submission_date": date.today().strftime("%d %B %Y"),
}

NAVY = RGBColor(0, 51, 102)
BLUE_HEAD = RGBColor(31, 78, 121)


def set_run(run, size=11, bold=False, color=None, name="Calibri"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    if color:
        run.font.color.rgb = color


def add_h(doc: Document, text: str, level: int = 1):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_run(r, size={1: 16, 2: 13, 3: 12}.get(level, 11), bold=True, color=NAVY)
    p.paragraph_format.space_before = Pt(12 if level == 1 else 8)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = level >= 2


def add_p(doc: Document, text: str):
    for block in text.strip().split("\n\n"):
        para = doc.add_paragraph(block.strip())
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        para.paragraph_format.line_spacing = 1.15
        para.paragraph_format.space_after = Pt(8)
        for run in para.runs:
            set_run(run)


def add_bullets(doc: Document, items: list[str]):
    for item in items:
        para = doc.add_paragraph(item, style="List Bullet")
        para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for run in para.runs:
            set_run(run)


def add_centered(doc: Document, text: str, size=12, bold=False, color=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    set_run(r, size=size, bold=bold, color=color or NAVY)


def add_pic(doc: Document, filename: str, width: float = 5.5, caption: str | None = None):
    path = IMG / filename
    if not path.exists():
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    p.add_run().add_picture(str(path), width=Inches(width))
    if caption:
        c = doc.add_paragraph(caption)
        c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in c.runs:
            set_run(run, size=9, color=RGBColor(90, 90, 90))


def set_col_widths(table, widths_in: list[float]):
    for row in table.rows:
        for idx, w in enumerate(widths_in):
            row.cells[idx].width = Inches(w)


def add_two_pics(doc: Document, left: str, right: str, width: float = 2.85):
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths(table, [3.1, 3.1])
    for cell, file in zip(table.rows[0].cells, (left, right)):
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        if (IMG / file).exists():
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(str(IMG / file), width=Inches(width))
    doc.add_paragraph()


def add_product_block(doc: Document, title: str, image: str, body: str):
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_col_widths(table, [2.5, 3.9])
    left, right = table.rows[0].cells
    left.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    right.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    if (IMG / image).exists():
        lp = left.paragraphs[0]
        lp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        lp.add_run().add_picture(str(IMG / image), width=Inches(2.35))
    rp = right.paragraphs[0]
    rp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    t = rp.add_run(title + "\n\n")
    set_run(t, bold=True, color=BLUE_HEAD, size=12)
    b = rp.add_run(body)
    set_run(b)
    doc.add_paragraph()


def style_profile_table(table):
    for row_idx, row in enumerate(table.rows):
        for cell in row.cells:
            tc_pr = cell._tc.get_or_add_tcPr()
            if row_idx == 0:
                shd = OxmlElement("w:shd")
                shd.set(qn("w:fill"), "1F4E79")
                tc_pr.append(shd)
            elif row_idx % 2 == 0:
                shd = OxmlElement("w:shd")
                shd.set(qn("w:fill"), "E8F1FA")
                tc_pr.append(shd)
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for run in p.runs:
                    if row_idx == 0:
                        set_run(run, bold=True, color=RGBColor(255, 255, 255))
                    else:
                        set_run(run, size=10)


def build_cover(doc: Document):
    add_centered(doc, "DIPLOMA FINAL-YEAR INTERNSHIP", 13, True)
    add_centered(doc, "COMPANY RESEARCH REPORT", 12, True, RGBColor(80, 80, 80))
    doc.add_paragraph()
    add_pic(doc, "tata_motors_logo.png", 1.5)
    add_centered(doc, "TATA MOTORS LIMITED", 18, True)
    add_centered(
        doc,
        "A Study of Company Development, Automotive Products,\n"
        "Research and Development, and Manufacturing Methodologies",
        11,
        False,
        RGBColor(70, 70, 70),
    )
    doc.add_paragraph()
    meta = [
        ("Submitted by", STUDENT["name"]),
        ("Diploma / Department", STUDENT["department"]),
        ("Institution", STUDENT["institution"]),
        ("Internship organisation", STUDENT["internship_org"]),
        ("Academic year", STUDENT["academic_year"]),
        ("Submission date", STUDENT["submission_date"]),
    ]
    table = doc.add_table(rows=len(meta), cols=2)
    table.style = "Table Grid"
    set_col_widths(table, [2.2, 4.2])
    for i, (k, v) in enumerate(meta):
        table.rows[i].cells[0].text = k
        table.rows[i].cells[1].text = v
    style_profile_table(table)
    doc.add_paragraph()
    add_centered(
        doc,
        "Submitted in partial fulfilment of the requirements for the Diploma final-year internship.",
        10,
        False,
        RGBColor(90, 90, 90),
    )


def build_docx() -> Path:
    doc = Document()
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    build_cover(doc)
    doc.add_page_break()

    add_h(doc, "Certificate / Declaration")
    add_p(
        doc,
        f"I hereby declare that this company research report entitled \"Tata Motors Limited — Company Research Report\" "
        f"is prepared by me, {STUDENT['name']}, as part of the final-year diploma internship requirement. The information "
        f"is compiled from publicly available sources with appropriate acknowledgement.\n\n"
        f"Place: Haveri\nDate: {STUDENT['submission_date']}\n\n"
        f"Signature of student: _______________________\nName: {STUDENT['name']}",
    )
    doc.add_page_break()

    add_h(doc, "Table of Contents")
    for line in [
        "Executive Summary",
        "1. Introduction",
        "2. About Tata Motors",
        "3. Company Overview (segments, achievements, R&D, sustainability)",
        "4. History and Development of Tata Motors",
        "5. Manufacturing Methodology Used by Tata Motors",
        "6. Products Manufactured by Tata Motors",
        "7. Challenges and Future Opportunities",
        "8. Research Methodology",
        "9. Conclusion",
        "References",
    ]:
        p = doc.add_paragraph(line)
        for run in p.runs:
            set_run(run)
    doc.add_page_break()

    add_h(doc, "Executive Summary")
    add_p(doc, EXECUTIVE_SUMMARY)
    add_pic(doc, "market_highlights.png", 5.4, "Figure ES-1: Market position highlights (FY25 public messaging)")
    doc.add_page_break()

    add_h(doc, "1. Introduction")
    add_p(doc, INTRO)

    add_h(doc, "2. About Tata Motors")
    add_p(doc, ABOUT)
    add_pic(doc, "photo_head_office.jpg", 5.6, "Figure 1: Tata Motors facility (reference image)")

    add_h(doc, "3. Company Overview")
    add_p(doc, OVERVIEW)
    add_pic(doc, "photo_overview.jpg", 5.8, "Figure 2: Manufacturing and product operations")
    add_pic(doc, "business_segments.png", 5.4, "Figure 3: Major business segments (illustrative)")
    add_h(doc, "3.1 Tata Commercial Vehicles (CV)", 2)
    add_p(doc, SEGMENT_CV_TEXT)
    add_bullets(doc, SEGMENT_CV)
    add_h(doc, "3.2 Tata Passenger Vehicles (PV)", 2)
    add_p(doc, SEGMENT_PV_TEXT)
    add_bullets(doc, SEGMENT_PV)
    add_h(doc, "3.3 Electric Mobility", 2)
    add_p(doc, SEGMENT_EV_TEXT)
    add_bullets(doc, SEGMENT_EV)
    add_h(doc, "3.4 Jaguar Land Rover (JLR)", 2)
    add_p(doc, SEGMENT_JLR)
    add_h(doc, "3.5 Achievements and business progress (FY2024–25)", 2)
    add_p(doc, ACHIEVEMENTS_FY25)
    add_h(doc, "3.6 Research, development and innovation", 2)
    add_p(doc, RD_INNOVATION)
    add_h(doc, "3.7 Sustainability and future mobility", 2)
    add_p(doc, SUSTAINABILITY)
    add_pic(doc, "ev_ecosystem.png", 5.2, "Figure 4: Electric mobility value chain")
    add_h(doc, "3.8 Core strengths", 2)
    add_bullets(doc, STRENGTHS)

    add_h(doc, "Basic company profile", 2)
    profile = doc.add_table(rows=11, cols=2)
    profile.style = "Table Grid"
    set_col_widths(profile, [2.0, 4.4])
    rows = [
        ("Particular", "Details"),
        ("Company name", "Tata Motors Limited"),
        ("Established", "1945"),
        ("Original name", "Tata Engineering and Locomotive Company (TELCO)"),
        ("Founder / group", "Founded under the leadership of the Tata Group"),
        ("Industry", "Automotive manufacturing"),
        ("Headquarters", "Mumbai, Maharashtra, India"),
        ("Parent group", "Tata Group"),
        ("Main products", "Cars, SUVs, trucks, buses, electric vehicles and mobility solutions"),
        ("Major markets", "India and selected international markets"),
        ("Key focus areas", "Quality, safety, innovation, sustainability and customer satisfaction"),
    ]
    for i, (a, b) in enumerate(rows):
        profile.rows[i].cells[0].text = a
        profile.rows[i].cells[1].text = b
    style_profile_table(profile)

    doc.add_page_break()

    add_h(doc, "4. History and Development of Tata Motors")
    add_two_pics(doc, "photo_history_collage.jpg", "photo_history_indica.jpg")
    add_pic(doc, "history_timeline.png", 5.6, "Figure 5: Historical milestone timeline")
    for title, body in HISTORY.items():
        add_h(doc, title, 2)
        add_p(doc, body)

    doc.add_page_break()

    add_h(doc, "5. Manufacturing Methodology Used by Tata Motors")
    add_two_pics(doc, "photo_manufacturing_robots.jpg", "photo_manufacturing_workers.jpg")
    add_p(doc, MFG_INTRO)
    add_pic(doc, "manufacturing_flow.png", 5.6, "Figure 6: Typical automobile manufacturing flow")
    for title, lead, bullets in MFG_SECTIONS:
        add_h(doc, title, 2)
        add_p(doc, lead)
        if bullets:
            add_bullets(doc, bullets)

    doc.add_page_break()

    add_h(doc, "6. Products Manufactured by Tata Motors")
    add_p(doc, PRODUCTS_INTRO)
    pt = doc.add_table(rows=len(PRODUCT_TABLE) + 1, cols=3)
    pt.style = "Table Grid"
    set_col_widths(pt, [1.4, 1.6, 3.4])
    hdr = pt.rows[0].cells
    hdr[0].text, hdr[1].text, hdr[2].text = "Segment", "Category", "Examples"
    for i, row in enumerate(PRODUCT_TABLE, start=1):
        for j, val in enumerate(row):
            pt.rows[i].cells[j].text = val
    style_profile_table(pt)
    doc.add_paragraph()

    for title, image, body in PRODUCT_BLOCKS:
        add_product_block(doc, title, image, body)

    add_h(doc, "6.5 Research, Development and Electronics (ECE relevance)", 2)
    add_p(doc, ECE)
    add_bullets(doc, ECE_BULLETS)
    add_pic(doc, "ece_automotive.png", 5.0, "Figure 7: Electronics integration in vehicles")
    add_h(doc, "6.6 Manufacturing plants in India", 2)
    add_p(doc, PLANTS)
    add_pic(doc, "india_plants_map.png", 4.8, "Figure 8: Major locations in India (schematic)")
    add_h(doc, "6.7 Internship and student programmes", 2)
    add_p(doc, INTERNSHIP_PROGRAMMES)
    add_pic(doc, "internship_value.png", 5.2, "Figure 9: Internship learning areas for diploma students")

    doc.add_page_break()

    add_h(doc, "7. Challenges and Future Opportunities")
    add_p(doc, CHALLENGES_INTRO)
    add_pic(doc, "photo_future_mobility.jpg", 5.4, "Figure 3: Future mobility and innovation")
    add_bullets(doc, CHALLENGES)

    add_h(doc, "8. Research Methodology")
    add_p(doc, METHODOLOGY)
    add_bullets(doc, METHODOLOGY_BULLETS)

    add_h(doc, "9. Conclusion")
    add_p(doc, CONCLUSION)

    add_h(doc, "References")
    for i, ref in enumerate(REFERENCES, 1):
        p = doc.add_paragraph(f"[{i}] {ref}")
        for run in p.runs:
            set_run(run, size=10)

    path = OUT / "TATA_Motors_Diploma_Project.docx"
    OUT.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    return path


def build_pdf_from_docx(docx_path: Path) -> Path:
    """Export PDF from DOCX so PDF matches Word layout and content exactly."""
    pdf_path = docx_path.with_suffix(".pdf")
    cmd = [
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        str(docx_path.parent),
        str(docx_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 or not pdf_path.exists():
        raise RuntimeError(
            "PDF export failed. Install LibreOffice (libreoffice-writer-nogui).\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )
    return pdf_path


def package(docx: Path, pdf: Path) -> Path:
    zip_path = OUT / "TATA_Motors_Diploma_Project_DOWNLOAD.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(docx, arcname=docx.name)
        zf.write(pdf, arcname=pdf.name)
    return zip_path


def main():
    docx = build_docx()
    pdf = build_pdf_from_docx(docx)
    zip_path = package(docx, pdf)
    print(docx)
    print(pdf)
    print(zip_path)


if __name__ == "__main__":
    main()
