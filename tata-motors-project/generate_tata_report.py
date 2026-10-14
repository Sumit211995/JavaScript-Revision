#!/usr/bin/env python3
"""Generate Tata Motors internship report — layout matched to student reference PDF."""

from __future__ import annotations

import zipfile
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from fpdf import FPDF

ROOT = Path(__file__).resolve().parent
IMG = ROOT / "images"
OUT = ROOT / "output"
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

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
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(6)


def add_p(doc: Document, text: str):
    for block in text.strip().split("\n\n"):
        para = doc.add_paragraph(block.strip())
        para.paragraph_format.line_spacing = 1.2
        para.paragraph_format.space_after = Pt(8)
        for run in para.runs:
            set_run(run)


def add_bullets(doc: Document, items: list[str]):
    for item in items:
        para = doc.add_paragraph(item, style="List Bullet")
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
    run = p.add_run()
    run.add_picture(str(path), width=Inches(width))
    if caption:
        c = doc.add_paragraph(caption)
        c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in c.runs:
            set_run(run, size=9, color=RGBColor(90, 90, 90))


def add_two_pics(doc: Document, left: str, right: str, width: float = 2.9):
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for cell, file in zip(table.rows[0].cells, (left, right)):
        if (IMG / file).exists():
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            cell.paragraphs[0].add_run().add_picture(str(IMG / file), width=Inches(width))
    doc.add_paragraph()


def add_product_block(doc: Document, title: str, image: str, body: str):
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False
    table.columns[0].width = Inches(2.6)
    table.columns[1].width = Inches(3.8)
    if (IMG / image).exists():
        c0 = table.rows[0].cells[0].paragraphs[0]
        c0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        c0.add_run().add_picture(str(IMG / image), width=Inches(2.4))
    c1 = table.rows[0].cells[1].paragraphs[0]
    r = c1.add_run(title + "\n")
    set_run(r, bold=True, color=BLUE_HEAD)
    r2 = c1.add_run(body)
    set_run(r2)
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
                for run in p.runs:
                    if row_idx == 0:
                        set_run(run, bold=True, color=RGBColor(255, 255, 255))
                    else:
                        set_run(run, size=10)


def build_cover(doc: Document):
    add_centered(doc, "DIPLOMA FINAL-YEAR INTERNSHIP", 13, True)
    add_centered(doc, "COMPANY RESEARCH REPORT", 12, True, RGBColor(80, 80, 80))
    doc.add_paragraph()
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
        f"I hereby declare that this report is my original work prepared for the diploma internship. "
        f"Information is taken from official and public sources with acknowledgement.\n\n"
        f"Place: Haveri\nDate: {STUDENT['submission_date']}\n\n"
        f"Signature: _______________________\nName: {STUDENT['name']}",
    )
    doc.add_page_break()

    add_h(doc, "Table of Contents")
    for line in [
        "1. Introduction",
        "2. About Tata Motors",
        "3. Company Overview",
        "4. History and Development of Tata Motors",
        "5. Manufacturing Methodology Used by Tata Motors",
        "6. Products Manufactured by Tata Motors",
        "7. Challenges and Future Opportunities",
        "8. Research Methodology",
        "9. Conclusion",
    ]:
        p = doc.add_paragraph(line)
        for run in p.runs:
            set_run(run)
    doc.add_page_break()

    # --- 1 Introduction ---
    add_h(doc, "1. Introduction")
    add_pic(doc, "tata_motors_logo.png", 1.6)
    add_p(
        doc,
        "The automobile industry is one of the most important sectors of the Indian economy. It "
        "contributes to industrial development, employment generation, technological innovation, "
        "infrastructure development, and international trade. Within this industry, Tata Motors has "
        "established itself as a major automobile manufacturer with a strong presence in passenger "
        "vehicles, commercial vehicles, electric mobility, and vehicle engineering.\n\n"
        "Tata Motors was established in 1945 as Tata Engineering and Locomotive Company Limited "
        "(TELCO). Initially, the company focused on manufacturing locomotives and engineering products. "
        "Over time, it expanded into commercial vehicles, passenger cars, sports utility vehicles (SUVs), "
        "buses, and electric vehicles. The company has contributed significantly to the development of "
        "the Indian automobile industry by introducing indigenous vehicle designs, expanding manufacturing "
        "capabilities, improving vehicle safety, and investing in sustainable mobility.\n\n"
        "This research report examines Tata Motors' background, organisational development, products, "
        "manufacturing processes, achievements, business progress, and recent developments. It also "
        "studies manufacturing methodologies and the importance of continuous improvement in quality, "
        "productivity, and customer satisfaction.",
    )

    # --- 2 About ---
    add_h(doc, "2. About Tata Motors")
    add_pic(doc, "photo_head_office.jpg", 5.8)
    add_p(
        doc,
        "Tata Motors is a well-known automotive manufacturer associated with the Tata Group. Its "
        "operations cover the design, development, manufacturing, marketing, and servicing of a wide "
        "range of vehicles.\n\n"
        "The company serves individual customers, businesses, logistics operators, public transport "
        "organisations, and industrial customers. Its vehicles are used for personal transportation, "
        "goods transportation, passenger transport, construction, and specialised commercial applications.\n\n"
        "Tata Motors has invested in research and development, vehicle electrification, connected "
        "technologies, safety engineering, and advanced manufacturing systems.",
    )

    # --- 3 Overview ---
    add_h(doc, "3. Company Overview")
    add_pic(doc, "photo_overview.jpg", 6.0)
    add_p(
        doc,
        "Tata Motors operates in a highly competitive industry where product quality, pricing, design, "
        "safety, technology, fuel efficiency, and after-sales service influence customer decisions. Its "
        "business developed around two principal segments:\n\n"
        "Passenger vehicles: Cars, SUVs and electric passenger vehicles for personal and family transportation.\n\n"
        "Commercial vehicles: Trucks, buses, vans, light commercial vehicles and specialised vehicles for "
        "businesses and public transportation.\n\n"
        "The group also includes electric mobility solutions and the global Jaguar Land Rover (JLR) business. "
        "Public reports for FY2024–25 note leadership in Indian CV, strong SUV growth in PV, and a large share "
        "of the passenger EV market.",
    )

    profile = doc.add_table(rows=10, cols=2)
    profile.style = "Table Grid"
    rows = [
        ("Particular", "Details"),
        ("Company name", "Tata Motors Limited"),
        ("Established", "1945"),
        ("Original name", "Tata Engineering and Locomotive Company (TELCO)"),
        ("Industry", "Automotive manufacturing"),
        ("Headquarters", "Mumbai, Maharashtra, India"),
        ("Parent group", "Tata Group"),
        ("Main products", "Cars, SUVs, trucks, buses, electric vehicles"),
        ("Major markets", "India and international markets"),
        ("Key focus", "Quality, safety, innovation, sustainability"),
    ]
    for i, (a, b) in enumerate(rows):
        profile.rows[i].cells[0].text = a
        profile.rows[i].cells[1].text = b
    style_profile_table(profile)

    doc.add_page_break()

    # --- 4 History ---
    add_h(doc, "4. History and Development of Tata Motors")
    add_two_pics(doc, "photo_history_collage.jpg", "photo_history_indica.jpg")
    add_h(doc, "4.1 Early foundation: 1945", 2)
    add_p(doc, "Tata Motors was established in 1945 as TELCO, with initial focus on locomotives and engineering products.")
    add_h(doc, "4.2 Entry into commercial vehicles: 1950s", 2)
    add_p(doc, "The company entered commercial vehicles through collaboration with Daimler-Benz (1954).")
    add_h(doc, "4.3 Expansion into passenger vehicles", 2)
    add_p(
        doc,
        "Passenger vehicles expanded the business beyond commercial transport. The Tata Indica (1998) "
        "became a milestone as an indigenously developed passenger car.",
    )
    add_h(doc, "4.4 International expansion: 2000s", 2)
    add_p(
        doc,
        "2004: Daewoo Commercial Vehicle Company (South Korea). 2008: Jaguar Land Rover acquired from Ford — "
        "a landmark global acquisition.",
    )
    add_h(doc, "4.5 Development of modern vehicles", 2)
    add_p(
        doc,
        "Modern lineup includes Tiago, Nexon, Harrier, Safari, Punch, and Curvv with improved safety, "
        "design, and technology.",
    )
    add_h(doc, "4.6 Electric mobility and digital manufacturing", 2)
    add_p(
        doc,
        "Investments in battery-electric vehicles, ZIPTRON powertrain, charging partnerships, connected "
        "features, automation, and sustainable mobility. FY25 milestones include expanded EV/CNG portfolio "
        "and new manufacturing capacity.",
    )

    # --- 5 Manufacturing ---
    add_h(doc, "5. Manufacturing Methodology Used by Tata Motors")
    add_two_pics(doc, "photo_manufacturing_robots.jpg", "photo_manufacturing_workers.jpg")
    add_p(
        doc,
        "Automobile manufacturing involves design, procurement, assembly, inspection, and delivery. "
        "The following are established practices relevant to Tata Motors operations (general industry methods; "
        "exact procedures vary by plant).",
    )
    mfg = [
        ("5.1 Lean manufacturing", "Reduces waste; improves flow of materials and work."),
        ("5.2 Just-in-Time (JIT)", "Supplies components when required on the production line."),
        ("5.3 Kaizen", "Continuous incremental improvement by employees and supervisors."),
        ("5.4 Total Quality Management", "Quality across design, production, and service—not only inspection."),
        ("5.5 Automation and robotics", "Improves precision and repeatability in welding and assembly."),
        ("5.6 CAD / CAM", "Digital design and manufacturing planning."),
        ("5.7 Supply chain management", "Vendor quality, inventory, scheduling, and logistics."),
        ("5.8 Safety and environment", "Occupational safety, emissions, waste, and compliance."),
        ("5.9 EV manufacturing", "Battery packs, high-voltage safety, motors, and power electronics."),
        ("5.10 Quality testing", "Body, paint, electrical, powertrain, brake, leak, and road tests."),
    ]
    for title, text in mfg:
        add_h(doc, title, 2)
        add_p(doc, text)

    doc.add_page_break()

    # --- 6 Products ---
    add_h(doc, "6. Products Manufactured by Tata Motors")
    add_p(
        doc,
        "Tata Motors has developed a wide range of vehicles for individual customers, businesses, and "
        "public transport operators.",
    )
    add_product_block(
        doc,
        "6.1 Passenger cars and SUVs",
        "product_passenger_suv.jpg",
        "Designed for personal and family transport. Examples: Tiago, Altroz, Tigor, Punch, Nexon, "
        "Harrier, Safari, and Curvv.",
    )
    add_product_block(
        doc,
        "6.2 Electric vehicles",
        "product_ev.jpg",
        "Battery-electric models such as Nexon EV, Tiago EV, Punch EV, and Tigor EV support lower emissions "
        "and sustainable mobility.",
    )
    add_product_block(
        doc,
        "6.3 Commercial trucks",
        "product_truck.jpg",
        "Used for goods movement across industries. Examples include Prima, Signa, Ultra, and Intra families.",
    )
    add_product_block(
        doc,
        "6.4 Buses and passenger transport",
        "product_bus.jpg",
        "Buses for city, school, staff, and intercity transport, including electric bus solutions.",
    )

    add_h(doc, "6.5 Relevance for ECE internship", 2)
    add_p(
        doc,
        "Electronics and Communication Engineering students may learn about wiring harnesses, ECU diagnostics, "
        "earthing and safety checks, BMS basics on EV lines, PLC automation, and end-of-line electrical testing "
        "during authorised plant training (e.g., Pune, Sanand, Jamshedpur).",
    )

    # --- 7 Challenges ---
    add_h(doc, "7. Challenges and Future Opportunities")
    add_pic(doc, "photo_future_mobility.jpg", 5.5)
    add_bullets(
        doc,
        [
            "Competition and pricing: balance features, affordability, and profitability.",
            "Supply chain resilience: semiconductors, batteries, and critical components.",
            "Quality and reliability: reduce defects, rework, and warranty costs.",
            "Electrification: charging infrastructure, battery cost, and customer confidence.",
            "Sustainability and compliance: safety and emission regulations.",
            "Opportunities: R&D, digitalisation, energy efficiency, and battery recycling.",
        ],
    )

    # --- 8 Methodology ---
    add_h(doc, "8. Research Methodology")
    add_p(
        doc,
        "Descriptive, document-based research using Tata Motors annual reports, investor presentations, "
        "official website, and automotive industry publications.",
    )
    add_bullets(
        doc,
        [
            "Secondary data: company reports, catalogues, government publications.",
            "Primary data (if performed): authorised plant visit and supervised discussions.",
            "Analysis: historical, descriptive, and thematic grouping.",
            "Limitations: confidential plant data is not publicly available.",
        ],
    )

    add_h(doc, "9. Conclusion")
    add_p(
        doc,
        "Tata Motors is a leading Indian automotive company with strong commercial and passenger portfolios, "
        "growing electric mobility, and global presence through JLR. Its manufacturing systems and electronics "
        "integration make it a valuable organisation for diploma internship and industrial learning.",
    )

    add_h(doc, "References")
    add_bullets(
        doc,
        [
            "Tata Motors Integrated Annual Report 2024–25.",
            "Tata Motors investor presentations and press releases (FY25).",
            "https://www.tatamotors.com",
            "https://joinus.tatamotors.com/student-programmes/",
        ],
    )

    path = OUT / "TATA_Motors_Diploma_Project.docx"
    OUT.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    return path


class ReportPDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 8)
        self.set_text_color(31, 78, 121)
        self.cell(0, 6, "TATA Motors | Company Research Report", align="L")
        self.ln(8)

    def footer(self):
        self.set_y(-12)
        self.set_draw_color(150, 40, 40)
        self.line(10, self.get_y(), 200, self.get_y())
        self.set_font("DejaVu", "", 8)
        self.set_text_color(80, 80, 80)
        self.cell(95, 8, "TATA Motors | Company Research Report")
        self.cell(95, 8, f"Page {self.page_no()}", align="R")


def pdf_block(pdf: ReportPDF, title: str, body: str):
    if pdf.get_y() > 250:
        pdf.add_page()
    pdf.set_x(pdf.l_margin)
    if title:
        pdf.set_font("DejaVu", "B", 12)
        pdf.set_text_color(0, 51, 102)
        pdf.multi_cell(pdf.epw, 6, title)
        pdf.ln(2)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.multi_cell(pdf.epw, 5.2, body)
    pdf.ln(4)


def pdf_image(pdf: ReportPDF, filename: str, w: float = 120):
    path = IMG / filename
    if not path.exists():
        return
    if pdf.get_y() > 200:
        pdf.add_page()
    x = pdf.l_margin + (pdf.epw - w) / 2
    pdf.image(str(path), x=x, w=w)
    pdf.ln(8)
    pdf.set_x(pdf.l_margin)


def build_pdf() -> Path:
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("DejaVu", "", f"{FONT_DIR}/DejaVuSans.ttf")
    pdf.add_font("DejaVu", "B", f"{FONT_DIR}/DejaVuSans-Bold.ttf")
    pdf.add_page()

    pdf.set_font("DejaVu", "B", 12)
    pdf.multi_cell(pdf.epw, 7, "DIPLOMA FINAL-YEAR INTERNSHIP\nCOMPANY RESEARCH REPORT", align="C")
    pdf.ln(2)
    pdf.set_font("DejaVu", "B", 16)
    pdf.multi_cell(pdf.epw, 8, "TATA MOTORS LIMITED", align="C")
    pdf.set_font("DejaVu", "", 10)
    pdf.multi_cell(
        pdf.epw,
        5,
        "A Study of Company Development, Automotive Products,\n"
        "Research and Development, and Manufacturing Methodologies",
        align="C",
    )
    pdf.ln(4)
    pdf_image(pdf, "tata_motors_logo.png", w=35)
    cover = (
        f"Submitted by: {STUDENT['name']}\n"
        f"Department: {STUDENT['department']}\n"
        f"Institution: {STUDENT['institution']}\n"
        f"Internship: {STUDENT['internship_org']}\n"
        f"Academic year: {STUDENT['academic_year']}\n"
        f"Date: {STUDENT['submission_date']}"
    )
    pdf.multi_cell(pdf.epw, 5.5, cover)
    pdf.add_page()

    sections = [
        ("1. Introduction", INTRO_TEXT, "tata_motors_logo.png", 28),
        ("2. About Tata Motors", ABOUT_TEXT, "photo_head_office.jpg", 150),
        ("3. Company Overview", OVERVIEW_TEXT, "photo_overview.jpg", 150),
        ("4. History and Development", HISTORY_TEXT, "photo_history_collage.jpg", 140),
        ("", "", "photo_history_indica.jpg", 140),
        ("5. Manufacturing Methodology", MFG_TEXT, "photo_manufacturing_robots.jpg", 85),
        ("", "", "photo_manufacturing_workers.jpg", 85),
        ("6. Products Manufactured", PRODUCTS_INTRO, None, 0),
        ("6.1 Passenger SUVs", PRODUCT_1, "product_passenger_suv.jpg", 70),
        ("6.2 Electric vehicles", PRODUCT_2, "product_ev.jpg", 70),
        ("6.3 Commercial trucks", PRODUCT_3, "product_truck.jpg", 70),
        ("6.4 Buses", PRODUCT_4, "product_bus.jpg", 70),
        ("7. Challenges & Opportunities", CHALLENGES_TEXT, "photo_future_mobility.jpg", 130),
        ("8. Research Methodology", METHOD_TEXT, None, 0),
        ("9. Conclusion", CONCLUSION_TEXT, None, 0),
    ]
    for title, body, img, w in sections:
        if title or body:
            pdf_block(pdf, title, body)
        if img and w:
            pdf_image(pdf, img, w=w)

    path = OUT / "TATA_Motors_Diploma_Project.pdf"
    pdf.output(str(path))
    return path


INTRO_TEXT = (
    "The automobile industry is vital to India's economy. Tata Motors (founded 1945 as TELCO) "
    "manufactures passenger vehicles, commercial vehicles, and electric mobility solutions. "
    "This report studies company development, products, R&D, and manufacturing methodologies."
)
ABOUT_TEXT = (
    "Tata Motors is part of the Tata Group and serves consumers, fleets, and public transport. "
    "It invests in electrification, connected technology, safety, and advanced manufacturing."
)
OVERVIEW_TEXT = (
    "Main segments: Passenger Vehicles (cars, SUVs, EVs) and Commercial Vehicles (trucks, buses, LCVs). "
    "The company competes on quality, safety, technology, and after-sales service."
)
HISTORY_TEXT = (
    "1945 TELCO; 1950s CV with Daimler-Benz; 1998 Indica; 2004 Daewoo; 2008 JLR; modern SUVs and EV leadership."
)
MFG_TEXT = (
    "Lean, JIT, Kaizen, TQM, automation, CAD/CAM, supply chain control, environmental management, "
    "EV battery safety, and end-of-line testing."
)
PRODUCTS_INTRO = "Wide portfolio for personal mobility, logistics, and public transport."
PRODUCT_1 = "Tiago, Altroz, Tigor, Punch, Nexon, Harrier, Safari, Curvv."
PRODUCT_2 = "Nexon EV, Tiago EV, Punch EV, Tigor EV."
PRODUCT_3 = "Prima, Signa, Ultra, Ace, Intra."
PRODUCT_4 = "Starbus and electric city buses."
CHALLENGES_TEXT = (
    "Competition, supply chain, quality, electrification, and regulation—balanced by R&D and digitalisation."
)
METHOD_TEXT = "Document-based research from official Tata Motors publications and industry sources."
CONCLUSION_TEXT = (
    "Tata Motors is a strong choice for diploma internship with exposure to large-scale automotive manufacturing."
)


def package(docx: Path, pdf: Path) -> Path:
    zip_path = OUT / "TATA_Motors_Diploma_Project_DOWNLOAD.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(docx, arcname=docx.name)
        zf.write(pdf, arcname=pdf.name)
    return zip_path


def main():
    docx = build_docx()
    pdf = build_pdf()
    zip_path = package(docx, pdf)
    print(docx)
    print(pdf)
    print(zip_path)


if __name__ == "__main__":
    main()
