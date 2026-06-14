import streamlit as st

# Your exact headers
st.text("=========================")
st.text("SCHOLARSHIP APPLICATION")
st.text("=========================")

# 1. Enter age input
age = st.number_input("Enter your age :", min_value=0, max_value=120, value=0)

# The logic checks once they actually type an age
if age > 0:
    if age >= 18:
        st.success("age requirement met . you can continue")

        # Your exact form inputs
        name = st.text_input("Enter your full name :")
        school = st.text_input("Enter your school :")
        birth = st.text_input("place of birth :")
        nationality = st.text_input("Enter your nationality :")

        # Show the completed summary if they've filled out their name
        if name:
            st.text("\n========================")
            st.text(" APPLICATION COMPLETED")
            st.text("========================")

            st.write(f"**name:** {name}")
            st.write(f"**school:** {school}")
            st.write(f"**birth:** {birth}")
            st.write(f"**nationality:** {nationality}")
            st.balloons() # Added a little celebration for finishing!

    else:
        # Your exact funny error message block!
        st.error("age requirement not met")
        st.warning("sorry oo 💔💔,😂 no be my fault 🫴 .")
        
        st.info("send 3k to 8061941988\nopay")
        st.text("\nTHANKS FOR BANKING WITH ME")
