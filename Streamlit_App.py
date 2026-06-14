import streamlit as st

# Website Header
st.title("=========================")
st.header("SCHOLARSHIP APPLICATION")
st.title("=========================")

# 1. Ask for age first using a number box
age = st.number_input("Enter your age:", min_value=0, max_value=120, value=0)

# 2. Check the age requirement when they look at the page
if age >= 18:
    st.success("Age requirement met. You can proceed with the application!")
    
    # Show the rest of the form fields
    name = st.text_input("Enter your full name:")
    school = st.text_input("Enter your school:")
    birth = st.text_input("Place of birth:")
    nationality = st.text_input("Enter your nationality:")
    
    # Submit button
    if st.button("Submit Application"):
        st.balloons()  # Adds a fun celebration effect!
        st.write(f"Thank you, {name}! Your application has been submitted.")
        
elif age > 0 and age < 18:
    st.error("Sorry, you must be 18 or older to apply for this scheme.")
