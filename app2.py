import streamlit as st
import json

st.set_page_config(layout="wide")

# -------------------------------
# Initialize session state
# -------------------------------
if "resume" not in st.session_state:
    st.session_state.resume = {
        "personal_info": {
            "name": "Raj Singh",
            "title": "Sr. HSE Manager",
            "email": "Raj.singh.hse@gmail.com",
            "phone": "+91 9883122847"
        },
        "skills": [],
        "achievements": [],
        "education": [],
        "certifications": [],
        "experience": []
    }

data = st.session_state.resume

# -------------------------------
# Layout: Left = Form | Right = Preview
# -------------------------------
col1, col2 = st.columns([1, 1])

# ===============================
# 🧾 LEFT SIDE (FORM BUILDER)
# ===============================
with col1:
    st.title("🛠 Resume Builder")

    # Personal Info
    st.subheader("Personal Info")
    data["personal_info"]["name"] = st.text_input("Name", data["personal_info"]["name"])
    data["personal_info"]["title"] = st.text_input("Title", data["personal_info"]["title"])
    data["personal_info"]["email"] = st.text_input("Email", data["personal_info"]["email"])
    data["personal_info"]["phone"] = st.text_input("Phone", data["personal_info"]["phone"])

    # Skills
    st.subheader("Skills")
    new_skill = st.text_input("Add Skill")
    if st.button("Add Skill"):
        if new_skill:
            data["skills"].append(new_skill)

    for i, skill in enumerate(data["skills"]):
        col_a, col_b = st.columns([4,1])
        col_a.write(skill)
        if col_b.button("❌", key=f"skill_{i}"):
            data["skills"].pop(i)

    # Achievements
    st.subheader("Achievements")
    ach_company = st.text_input("Company (Achievement)")
    ach_text = st.text_input("Achievement")

    if st.button("Add Achievement"):
        if ach_company and ach_text:
            found = next((a for a in data["achievements"] if a["company"] == ach_company), None)
            if found:
                found["items"].append(ach_text)
            else:
                data["achievements"].append({
                    "company": ach_company,
                    "items": [ach_text]
                })

    # Experience
    st.subheader("Experience")

    exp_company = st.text_input("Company")
    exp_role = st.text_input("Role")
    exp_duration = st.text_input("Duration")
    exp_project = st.text_input("Project Name")
    exp_detail = st.text_input("Responsibility")

    if st.button("Add Experience"):
        if exp_company and exp_project and exp_detail:
            company = next((e for e in data["experience"] if e["company"] == exp_company), None)

            if not company:
                company = {
                    "company": exp_company,
                    "role": exp_role,
                    "duration": exp_duration,
                    "projects": []
                }
                data["experience"].append(company)

            project = next((p for p in company["projects"] if p["name"] == exp_project), None)

            if not project:
                project = {
                    "name": exp_project,
                    "details": []
                }
                company["projects"].append(project)

            project["details"].append(exp_detail)

    # Export JSON
    st.subheader("Export")
    st.download_button(
        "📥 Download JSON",
        data=json.dumps(data, indent=2),
        file_name="resume.json",
        mime="application/json"
    )

# ===============================
# 👀 RIGHT SIDE (LIVE PREVIEW)
# ===============================
with col2:
    st.title("📄 Live Preview")

    info = data["personal_info"]
    st.markdown(f"## {info['name']}")
    st.write(info["title"])
    st.write(f"📧 {info['email']} | 📱 {info['phone']}")

    # Skills
    st.subheader("Skills")
    for skill in data["skills"]:
        st.markdown(f"- {skill}")

    # Achievements
    st.subheader("Achievements")
    for ach in data["achievements"]:
        st.markdown(f"**{ach['company']}**")
        for item in ach["items"]:
            st.markdown(f"✔ {item}")

    # Experience
    st.subheader("Experience")
    for exp in data["experience"]:
        st.markdown(f"### {exp['company']} | {exp['role']} ({exp['duration']})")
        for proj in exp["projects"]:
            st.markdown(f"**{proj['name']}**")
            for d in proj["details"]:
                st.markdown(f"- {d}")