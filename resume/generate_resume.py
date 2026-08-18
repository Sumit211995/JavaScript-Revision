#!/usr/bin/env python3
"""Generate Sumit Kaktwan resume as one-page DOCX and PDF (ATS-friendly)."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from fpdf import FPDF

OUT = Path(__file__).resolve().parent
NAVY = (31, 78, 121)
BODY = (33, 33, 33)
MUTED = (70, 70, 70)
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

SUMMARY = (
    "Frontend Engineer with 3 years of experience building production React.js and Next.js "
    "applications, including role-based admin dashboards, warranty and claim workflows, and "
    "CMS-backed websites. Skilled in TypeScript, RBAC, REST API integration, Redux, Zustand, "
    "and deployments on Railway and Linux VMs. Owned end-to-end frontend for solar manufacturing, "
    "travel, and enterprise meeting products, and guided 2-3 frontend developers on selected projects."
)

SKILLS = [
    ("Languages: ", "JavaScript (ES6+), TypeScript, HTML5, CSS3, SCSS"),
    (
        "Frontend: ",
        "React.js, Next.js, Redux, Zustand, React Hook Form, Zod, Tailwind CSS, Responsive Web Design",
    ),
    (
        "Integration: ",
        "REST APIs, Payload CMS, PostgreSQL, Azure Functions, Microsoft Graph API, Firebase, Google Maps API",
    ),
    (
        "Tools: ",
        "Git, GitHub, Railway, Linux VM, Agile, Code Review, UI/UX implementation",
    ),
]

EMMVEE_BULLETS = [
    "Owned frontend for five production apps in React.js, Next.js, and TypeScript: Prism (solar shop floor), warranty and claims, Board Meeting and Committee (BMC), Roamiyo travel admin, and the Emmvee Foundation website.",
    "Built Prism dashboards with RBAC for QA, Production, PPC, Admin, Super Admin, and Manager, including line and module reports.",
    "Developed the React.js warranty portal with Zustand authentication for 15+ roles (homeowner, distributor, CSR, QA, Finance, Sales, and others). Covered invoice and PSN transfer, claim intake, QA assignment, refund, replacement, and rework tickets, multi-level approvals, and certificate download.",
    "Implemented BMC in Next.js, Tailwind CSS, and SCSS for Microsoft Teams-connected meetings: create, approve, cancel, reject, agendas, attendance, action items, AI-generated minutes of meeting (MOM), documents, and user management. Backend used Microsoft Graph API.",
    "Built the Roamiyo admin dashboard in Next.js (customers, flights, stays, transactions, tickets, itineraries, charts) and contributed to the production RoamWithRoamiyo web app using Redux, Azure Functions, and Next.js.",
    "Delivered the Foundation website with Next.js, Payload CMS, and PostgreSQL, including customized admin CSS. Deployed Foundation and BMC on Railway; deployed Prism and Warranty on a Linux VM.",
    "Acted as sole frontend owner on most products and guided 2-3 frontend developers on selected projects.",
]

TRIFLER_BULLETS = [
    "Built a multi-step partner onboarding dashboard with React Hook Form, Zod validation, token-based authentication, Google Maps API, and Firebase event logging.",
    "Developed a Next.js and TypeScript admin dashboard for user and partner management and a blog CMS.",
    "Collaborated with design and backend teams on product features, code reviews, debugging, and maintainable UI.",
]

CERTS = (
    "JavaScript and React.js, NamasteDev; Web Development, Udemy; Core Java, Smart Programming"
)


def set_run_font(run, name="Calibri", size=10, bold=False, color=None):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run._element.rPr.rFonts.set(qn("w:ascii"), name)
    run._element.rPr.rFonts.set(qn("w:hAnsi"), name)
    run.font.size = Pt(size)
    run.bold = bold
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_bottom_border(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "1F4E79")
    pBdr.append(bottom)
    pPr.append(pBdr)


def tight_paragraph(doc, space_before=0, space_after=0):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = 1.0
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    pf.widow_control = True
    return p


def heading_para(doc, text):
    p = tight_paragraph(doc, space_before=4, space_after=2)
    run = p.add_run(text.upper())
    set_run_font(run, size=10.5, bold=True, color=NAVY)
    add_bottom_border(p)
    return p


def bullet(doc, text):
    p = tight_paragraph(doc, space_before=0, space_after=1)
    p.paragraph_format.left_indent = Inches(0.16)
    p.paragraph_format.first_line_indent = Inches(-0.13)
    run = p.add_run("- " + text)
    set_run_font(run, size=10)
    return p


def job_header(doc, left, right):
    p = tight_paragraph(doc, space_before=3, space_after=0)
    set_run_font(p.add_run(left), size=10, bold=True)
    set_run_font(p.add_run("\t" + right), size=9.5)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(7.15), WD_TAB_ALIGNMENT.RIGHT)
    return p


def job_sub(doc, left, right):
    p = tight_paragraph(doc, space_before=0, space_after=1)
    set_run_font(p.add_run(left), size=9.5, color=MUTED)
    set_run_font(p.add_run("\t" + right), size=9.5, color=MUTED)
    p.paragraph_format.tab_stops.add_tab_stop(Inches(7.15), WD_TAB_ALIGNMENT.RIGHT)
    return p


def build_docx(path):
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(9.5)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.line_spacing = 1.0

    for section in doc.sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.45)
        section.left_margin = Inches(0.55)
        section.right_margin = Inches(0.55)
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.different_first_page_header_footer = False

    name = tight_paragraph(doc, 0, 0)
    name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run_font(name.add_run("SUMIT KAKTWAN"), size=16, bold=True, color=NAVY)

    contact = tight_paragraph(doc, 1, 0)
    contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run_font(
        contact.add_run(
            "Bengaluru, Karnataka, India  |  +91-9997776729  |  sumitcskaktwan@gmail.com"
        ),
        size=10,
    )
    contact2 = tight_paragraph(doc, 0, 1)
    contact2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run_font(
        contact2.add_run(
            "https://www.linkedin.com/in/sumit-kaktwan-270633157  |  https://github.com/Sumit211995"
        ),
        size=10,
    )

    heading_para(doc, "Professional Summary")
    s = tight_paragraph(doc, 1, 1)
    set_run_font(s.add_run(SUMMARY), size=10)

    heading_para(doc, "Technical Skills")
    for label, rest in SKILLS:
        p = tight_paragraph(doc, 1, 1)
        set_run_font(p.add_run(label), size=10, bold=True)
        set_run_font(p.add_run(rest), size=10)

    heading_para(doc, "Professional Experience")
    job_header(doc, "Emmvee Technology Pvt. Ltd. (Emmvee Photovoltaic)", "Bengaluru, India")
    job_sub(doc, "Frontend Engineer", "15 Sep 2025 - Present")
    for t in EMMVEE_BULLETS:
        bullet(doc, t)

    job_header(doc, "Trifler India (Aquonics Tech Service Pvt. Ltd.)", "Bengaluru, India")
    job_sub(doc, "Frontend Developer", "Oct 2023 - 12 Sep 2025")
    for t in TRIFLER_BULLETS:
        bullet(doc, t)

    job_header(doc, "Satyam Auto Component  |  Tata Motors", "Gurugram / Pantnagar, India")
    job_sub(
        doc,
        "Engineer  |  Junior Associate, Lean Manufacturing",
        "May 2019 - Jul 2020  |  Aug 2014 - Apr 2019",
    )
    bullet(
        doc,
        "MOST, line balancing, kaizen, ergonomics, and cost reduction in automotive manufacturing. This domain background supports solar production UIs such as Prism.",
    )

    heading_para(doc, "Education")
    job_header(doc, "DIT University, Dehradun", "Uttarakhand, India")
    job_sub(
        doc,
        "Bachelor of Technology in Computer Science and Engineering  |  CGPA 7.7/10",
        "Aug 2020 - Jun 2023",
    )

    heading_para(doc, "Certifications")
    p = tight_paragraph(doc, 1, 0)
    set_run_font(p.add_run(CERTS), size=10)

    doc.save(path)


class ResumePDF(FPDF):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_font("DejaVu", "", f"{FONT_DIR}/DejaVuSans.ttf")
        self.add_font("DejaVu", "B", f"{FONT_DIR}/DejaVuSans-Bold.ttf")

    def footer(self):
        pass


def pdf_section(pdf, title):
    pdf.ln(3.0)
    pdf.set_font("DejaVu", "B", 11)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 5.5, title.upper(), new_x="LMARGIN", new_y="NEXT")
    y = pdf.get_y()
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.4)
    pdf.line(12, y, 198, y)
    pdf.ln(2.0)
    pdf.set_text_color(*BODY)


def pdf_job(pdf, company, loc, title, dates):
    pdf.set_font("DejaVu", "B", 10)
    pdf.set_text_color(*BODY)
    pdf.cell(125, 4.6, company, align="L")
    pdf.set_font("DejaVu", "", 9.5)
    pdf.cell(0, 4.6, loc, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(*MUTED)
    pdf.cell(115, 4.6, title, align="L")
    pdf.cell(0, 4.6, dates, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(*BODY)


def pdf_bullet(pdf, text):
    pdf.set_font("DejaVu", "", 9.5)
    pdf.set_x(14)
    pdf.multi_cell(182, 4.25, "- " + text)
    pdf.ln(0.65)


def build_pdf(path):
    pdf = ResumePDF(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=14)
    pdf.add_page()
    pdf.set_margins(12, 14, 12)

    pdf.set_font("DejaVu", "B", 18)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 9, "SUMIT KAKTWAN", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("DejaVu", "", 9.5)
    pdf.set_text_color(*BODY)
    pdf.cell(
        0,
        5,
        "Bengaluru, Karnataka, India  |  +91-9997776729  |  sumitcskaktwan@gmail.com",
        align="C",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.cell(
        0,
        5,
        "https://www.linkedin.com/in/sumit-kaktwan-270633157  |  https://github.com/Sumit211995",
        align="C",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf_section(pdf, "Professional Summary")
    pdf.set_font("DejaVu", "", 9.5)
    pdf.multi_cell(0, 4.2, SUMMARY)

    pdf_section(pdf, "Technical Skills")
    for label, rest in SKILLS:
        pdf.set_font("DejaVu", "B", 9.5)
        pdf.write(4.2, label)
        pdf.set_font("DejaVu", "", 9.5)
        pdf.write(4.2, rest)
        pdf.ln(5.1)

    pdf_section(pdf, "Professional Experience")
    pdf_job(
        pdf,
        "Emmvee Technology Pvt. Ltd. (Emmvee Photovoltaic)",
        "Bengaluru, India",
        "Frontend Engineer",
        "15 Sep 2025 - Present",
    )
    for t in EMMVEE_BULLETS:
        pdf_bullet(pdf, t)

    pdf_job(
        pdf,
        "Trifler India (Aquonics Tech Service Pvt. Ltd.)",
        "Bengaluru, India",
        "Frontend Developer",
        "Oct 2023 - 12 Sep 2025",
    )
    for t in TRIFLER_BULLETS:
        pdf_bullet(pdf, t)

    pdf_job(
        pdf,
        "Satyam Auto Component  |  Tata Motors",
        "Gurugram / Pantnagar, India",
        "Engineer  |  Junior Associate, Lean Manufacturing",
        "May 2019 - Jul 2020  |  Aug 2014 - Apr 2019",
    )
    pdf_bullet(
        pdf,
        "MOST, line balancing, kaizen, ergonomics, and cost reduction in automotive manufacturing. This domain background supports solar production UIs such as Prism.",
    )

    pdf_section(pdf, "Education")
    pdf_job(
        pdf,
        "DIT University, Dehradun",
        "Uttarakhand, India",
        "Bachelor of Technology in Computer Science and Engineering  |  CGPA 7.7/10",
        "Aug 2020 - Jun 2023",
    )

    pdf_section(pdf, "Certifications")
    pdf.set_font("DejaVu", "", 9.5)
    pdf.multi_cell(0, 4.2, CERTS)

    pdf.output(path)


if __name__ == "__main__":
    docx_path = OUT / "Sumit_Kaktwan_Frontend_Resume.docx"
    pdf_path = OUT / "Sumit_Kaktwan_Frontend_Resume.pdf"
    build_docx(docx_path)
    build_pdf(pdf_path)
    print(docx_path)
    print(pdf_path)
