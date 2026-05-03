import streamlit as st

# Title
st.title("Raj Singh - Sr. HSE Manager")

# Contact Info
st.write("📧 Raj.singh.hse@gmail.com")
st.write("📱 +91 9883122847")

# Skills Section
st.header("Skills")
skills = [
    "Effective implementation of JSA, HIRA, SIMOPS, PTW systems",
    "Contractor HSE evaluation, onboarding, monitoring, stop-work authority",
    "Incident investigation, root cause analysis, lesson sharing",
    "Compliance with waste management, emissions, biodiversity, land use",
    "Leading & lagging HSE indicators tracking",
    "HSE dashboards, trend analysis, safety maturity assessments",
    "Authority to stop unsafe work & escalate risks",
    "ISO 45001, ISO 14001, ISO 9001 compliance",
    "Digital HSE initiatives (dashboards, predictive analytics)",
    "Leadership safety programs"
]
for skill in skills:
    st.markdown(f"- {skill}")

# Achievements
st.header("Key Achievements")
st.subheader("Technip Energies")
st.write("✅ 34M Safe Man Hours (HURL Barauni, Bihar)")
st.write("✅ 22M Safe Man Hours (HRRL Barmer, Rajasthan)")
st.write("✅ AI Vision Cameras for HSE monitoring")
st.write("✅ Digital BBS program implementation")

st.subheader("Larsen & Toubro")
st.write("✅ SLD risk assessment methodology")
st.write("✅ HSE Knowledge retention program")

st.subheader("TATA Projects Limited")
st.write("✅ KRA for execution team")
st.write("✅ Leadership Engagement Sponsorship program")

# Education
st.header("Education")
st.write("🎓 B.Tech Mechanical Engineering - Dr MGR Educational & Research Institute")
st.write("🎓 M.Tech Industrial Safety Engineering - RGPV State Technical University")

# Certifications
st.header("Certifications")
certs = [
    "IOSH Managing Safely",
    "ISO 45001:2018 Internal Auditor",
    "NEBOSH IGC & Diploma DI1",
    "Industrial Safety Engineering (IIT Kharagpur - NPTEL)"
]
for cert in certs:
    st.markdown(f"- {cert}")

# Experience
st.header("Professional Experience")
st.write("**Technip Energies India Limited** - Sr. Manager HSE (2019 - Present)")
st.write("**Tata Projects Limited** - Dy. Manager HSE (2016 - 2019)")
st.write("**Larsen & Toubro Limited** - Sr. HSE Engineer (2015 - 2016)")
st.write("**Ask EHS (Reliance Industries)** - Safety Engineer (2014 - 2015)")
st.write("**Lloyd Insulation Limited** - Safety Officer (2013 - 2014)")
st.write("**Johnson Pvt Ltd** - Safety Officer (2013)")
st.write("**Shreeji Asia Pvt Ltd** - Safety Officer (2012 - 2013)")
st.write("**Anand Engineering & Construction** - Mechanical Erection Engineer (2010 - 2012)")
