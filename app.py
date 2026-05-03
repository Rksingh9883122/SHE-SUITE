st.set_page_config(
    page_title="HSE SUITE",
    page_icon="📄",
    layout="wide"
)



import streamlit as st
from fpdf import FPDF
from docx import Document
import data
import os
import io
import textwrap

# -------------------------------
# Title & Picture
# -------------------------------
st.title("Raj Singh - Sr. HSE Manager")

if os.path.exists("profile.jpg"):
    st.image("profile.jpg", width=200)
else:
    st.warning("Profile picture not found. Please add 'profile.jpg'")

# -------------------------------
# Contact Info
# -------------------------------
st.write("📧 Raj.singh.hse@gmail.com")
st.write("📱 +91 9883122847")

# -------------------------------
# Skills
# -------------------------------
st.header("Skills")
for skill in data.skills:
    st.markdown(f"- {skill}")

# -------------------------------
# Achievements
# -------------------------------
st.header("Key Achievements")
for company, items in data.achievements.items():
    st.subheader(company)
    for item in items:
        st.write(f"✅ {item}")

# -------------------------------
# Education
# -------------------------------
st.header("Education")
for edu in data.education:
    st.write(f"🎓 {edu}")

# -------------------------------
# Certifications
# -------------------------------
st.header("Certifications")
for cert in data.certifications:
    st.markdown(f"- {cert}")

# -------------------------------
# Experience
# -------------------------------
st.header("Professional Experience")
for exp in data.experience:
    st.subheader(f"{exp['role']} - {exp['company']}")
    for point in exp["details"]:
        st.write(f"• {point}")

# -------------------------------
# PDF Export Function
# -------------------------------
def create_pdf():
    pdf = FPDF()

    # Use Windows Arial Unicode
    font_path = "C:/Windows/Fonts/arial.ttf"
    pdf.add_font("ArialUnicode", "", font_path, uni=True)

    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_font("ArialUnicode", "", 12)

    # margins
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)

    page_width = pdf.w - pdf.l_margin - pdf.r_margin

    # Title
    pdf.set_font("ArialUnicode", "", 14)
    pdf.cell(page_width, 10, "Raj Singh - Sr. HSE Manager", ln=1, align="C")

    pdf.set_font("ArialUnicode", "", 11)
    pdf.cell(page_width, 8, "Contact: Raj.singh.hse@gmail.com | +91 9883122847", ln=1)
    pdf.ln(4)

    # -------- Skills --------
    pdf.set_x(pdf.l_margin)
    pdf.cell(page_width, 8, "Skills:", ln=1)

    for skill in data.skills:
        pdf.set_x(pdf.l_margin)
        wrapped = "\n".join(textwrap.wrap(skill, 85))
        pdf.multi_cell(page_width, 7, f"- {wrapped}")
    pdf.ln(2)

    # -------- Achievements --------
    pdf.set_x(pdf.l_margin)
    pdf.cell(page_width, 8, "Achievements:", ln=1)

    for company, items in data.achievements.items():
        pdf.set_x(pdf.l_margin)
        pdf.cell(page_width, 7, company, ln=1)

        for item in items:
            pdf.set_x(pdf.l_margin)
            wrapped = "\n".join(textwrap.wrap(item, 85))
            pdf.multi_cell(page_width, 7, f"- {wrapped}")
    pdf.ln(2)

    # -------- Education --------
    pdf.set_x(pdf.l_margin)
    pdf.cell(page_width, 8, "Education:", ln=1)

    for edu in data.education:
        pdf.set_x(pdf.l_margin)
        wrapped = "\n".join(textwrap.wrap(edu, 85))
        pdf.multi_cell(page_width, 7, f"- {wrapped}")
    pdf.ln(2)

    # -------- Certifications --------
    pdf.set_x(pdf.l_margin)
    pdf.cell(page_width, 8, "Certifications:", ln=1)

    for cert in data.certifications:
        pdf.set_x(pdf.l_margin)
        wrapped = "\n".join(textwrap.wrap(cert, 85))
        pdf.multi_cell(page_width, 7, f"- {wrapped}")
    pdf.ln(2)

    # -------- Experience --------
    pdf.set_x(pdf.l_margin)
    pdf.cell(page_width, 8, "Experience:", ln=1)

    for exp in data.experience:
        company = exp.get("company", "")
        role = exp.get("role", "")
        details = exp.get("details", [])

        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(page_width, 7, f"{role} - {company}")

        for point in details:
            pdf.set_x(pdf.l_margin)
            wrapped = "\n".join(textwrap.wrap(point, 85))
            pdf.multi_cell(page_width, 7, f"- {wrapped}")

        pdf.ln(1)

    # Output safely
    pdf_out = pdf.output(dest="S")

    if isinstance(pdf_out, str):
        return pdf_out.encode("latin-1")
    else:
        return bytes(pdf_out)


# -------------------------------
# Word Export Function
# -------------------------------
def create_word():
    doc = Document()

    doc.add_heading("Raj Singh - Sr. HSE Manager", 0)
    doc.add_paragraph("Contact: Raj.singh.hse@gmail.com | +91 9883122847")

    doc.add_heading("Skills", 1)
    for skill in data.skills:
        doc.add_paragraph(skill, style="List Bullet")

    doc.add_heading("Achievements", 1)
    for company, items in data.achievements.items():
        doc.add_heading(company, 2)
        for item in items:
            doc.add_paragraph(item, style="List Bullet")

    doc.add_heading("Education", 1)
    for edu in data.education:
        doc.add_paragraph(edu, style="List Bullet")

    doc.add_heading("Certifications", 1)
    for cert in data.certifications:
        doc.add_paragraph(cert, style="List Bullet")

    doc.add_heading("Experience", 1)
    for exp in data.experience:
        company = exp.get("company", "")
        role = exp.get("role", "")
        details = exp.get("details", [])

        doc.add_paragraph(f"{role} - {company}", style="List Bullet")
        for point in details:
            doc.add_paragraph(point, style="List Bullet 2")

    bio = io.BytesIO()
    doc.save(bio)
    return bio.getvalue()


# -------------------------------
# Download Buttons
# -------------------------------
st.write("---")

pdf_data = create_pdf()
st.download_button("📄 Download Profile as PDF", pdf_data, "Raj_Singh_Profile.pdf")

word_data = create_word()
st.download_button("📝 Download Profile as Word", word_data, "Raj_Singh_Profile.docx")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)