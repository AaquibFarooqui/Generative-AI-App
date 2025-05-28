import streamlit as st
from transformers import pipeline, set_seed


def generate_hospital_prescription(patient_info, doctor_instructions, hospital_info, doctor_info):
    """
    Generate a dynamic medical prescription based on patient details, doctor's notes, and hospital information.
    Includes specific medicine names, dosages, precautions, and structured format with hospital and doctor details.

    Args:
    - patient_info (dict): Contains patient-specific details (e.g., age, gender, symptoms, medical history).
    - doctor_instructions (str): Notes provided by the doctor outlining the patient's condition or treatment goals.
    - hospital_info (dict): Contains hospital details like name, address, and contact number.
    - doctor_info (dict): Contains doctor's details like name and registration number.

    Returns:
    - str: A structured medical prescription in the format of a hospital.
    """
    # Initialize the text-generation pipeline
    generator = pipeline("text-generation", model="gpt2")

    # Ensure reproducible results
    set_seed(42)

    # Constructing the prompt for dynamic prescription generation
    prompt = f"""
    Patient Details:
    Age: {patient_info['age']}
    Gender: {patient_info['gender']}
    Symptoms: {', '.join(patient_info['symptoms'])}
    Medical History: {patient_info['medical_history']}

    Doctor's Notes:
    {doctor_instructions}

    Based on the above information, your task is to:
    1. Suggest appropriate medicines tailored to the patient's condition.
    2. Provide specific dosages for morning, noon, and evening.
    3. Offer relevant advice and lifestyle recommendations for recovery.
    4. Include precautions that the patient should follow to avoid complications.
    Ensure the prescription is medically accurate and personalized for the patient's condition.

    Prescription Format:
    Hospital Name: {hospital_info['name']}
    Address: {hospital_info['address']}
    Contact Number: {hospital_info['contact_number']}

    Doctor Name: {doctor_info['name']}
    Registration Number: {doctor_info['registration_number']}
    """
    
    # Generate the dynamic prescription
    result = generator(
        prompt,
        max_length=400,  # Allow more space for detailed responses
        num_return_sequences=1,
        temperature=0.7,
        truncation=True,  # Explicitly enable truncation
        pad_token_id=50256  # Use the end-of-sequence token for padding
    )

    # Combine hospital and doctor details with the generated content
    prescription = f"""
    Hospital Details:
    {hospital_info['name']}
    Address: {hospital_info['address']}
    Contact Number: {hospital_info['contact_number']}

    Doctor Details:
    Name: {doctor_info['name']}
    Registration Number: {doctor_info['registration_number']}

    Patient Details:
    Age: {patient_info['age']}
    Gender: {patient_info['gender']}
    Symptoms: {', '.join(patient_info['symptoms'])}
    Medical History: {patient_info['medical_history']}

    Doctor's Notes:
    {doctor_instructions}

    Prescription:
    {result[0]['generated_text'].strip()}
    """
    
    return prescription



hospital_details = {
    "name": "City Health Hospital\n",
    "address": "123 Main Street, Mumbai, Maharashtra, India\n",
    "contact_number": "+91 9876543210"
}

doctor_details = {
    "name": "Dr. Rajesh Sharma",
    "registration_number": "MED123456"
}


# Create an empty container
placeholder = st.empty()


patient_info = {}
doctor_notes =""

# Insert a form in the container
with placeholder.form("Generate Prescription"):
    st.markdown("#### Generate Prescription")
    age = st.text_input("Enter Age")
    gender = st.text_input("Patient Gender")
    symptoms = st.text_input("Symptoms (comma-separated): ").split(", ")
    medical_history = st.text_input("Medical History")

    patient_info = {
        "age": age,
        "gender": gender,
        "symptoms": symptoms,
        "medical_history": medical_history
    }

    doctor_notes = st.text_input("Doctor's Notes:")
    
    submit = st.form_submit_button("Generate")

if submit:
    hospital_prescription = generate_hospital_prescription(patient_info, doctor_notes, hospital_details, doctor_details)
    

    placeholder.empty()
    #st.markdown(response.text)
    st.success(hospital_prescription)
   
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass
