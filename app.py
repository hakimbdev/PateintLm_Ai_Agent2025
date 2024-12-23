import http.client
import streamlit as st

# Streamlit App Title
st.title("PatientLm")
st.write("Explain your health problem and get immediate solutions.")

# Optional: User Input (if required by the API)
user_input = st.text_input("Describe your symptoms or health problem:")

# API Call Function
def get_health_data():
    conn = http.client.HTTPSConnection("the-retreat-clinic.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "d8918ac8a5msh6cb631dc4231223p10594ajsnbec1f96e6692",
        'x-rapidapi-host': "the-retreat-clinic.p.rapidapi.com"
    }
    conn.request("GET", "/", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

# Button to Trigger API Call
if st.button("Get Prescription Advice"):
    if user_input:
        st.write("Fetching results for your input...")
        try:
            response = get_health_data()
            st.success("Response received!")
            st.json(response)  # Display JSON response
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please describe your symptoms before proceeding.")

# Footer
st.write("---")
st.write("Developed by Abdulhakim Ahmad")
