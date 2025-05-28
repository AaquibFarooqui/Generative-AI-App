import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

project_3_page = st.Page(
    "views/Diet.py",
    title="Fitness Diet Chatboat",
    icon=":material/smart_toy:",
)

project_4_page = st.Page(
    "views/prescription.py",
    title="HealthCare Prescription",
    icon=":material/smart_toy:",
)

project_5_page = st.Page(
    "views/fashion.py",
    title="Fashion Assistant",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Generative AI LLM": [project_3_page,project_4_page,project_5_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/codingisfun_logo.png")


st.sidebar.markdown("Made ❤️ by [Jagdish Gopchandani]")


# --- RUN NAVIGATION ---
pg.run()
