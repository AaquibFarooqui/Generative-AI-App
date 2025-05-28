import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyCZRtlAdnLu6sH3p-EkjifaQaVzuyTGGt0")


# Create an empty container
placeholder = st.empty()

que=""

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Fitness Diet Chat GPT")
    que = st.text_input("Enter Query")
    
    submit = st.form_submit_button("Ask Me")

if submit:
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=que,
    )

    placeholder.empty()
    #st.markdown(response.text)
    st.success(response.text)
else:
    pass
