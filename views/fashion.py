import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyCZRtlAdnLu6sH3p-EkjifaQaVzuyTGGt0")


# Create an empty container
placeholder = st.empty()

que=""

# Insert a form in the container
with placeholder.form("Fashion Recommendation"):
    st.markdown("#### Fashion Recommendation Assistant")
    que = st.text_input("How Can I Help You")
    
    submit = st.form_submit_button("Ask Me")

if submit:
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=que,
    )

    placeholder.empty()
    #st.markdown(response.text)
    st.success(response.text)
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass
