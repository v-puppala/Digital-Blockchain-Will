import streamlit as st

#input field
ssn = st.sidebar.text_input("Enter your Social Security Number:", type="password")

#check if input meets length requirements
if len(ssn) !=9:
    st.error("SSN must be 9 digits long.")
if ssn.isdigit()==False:
    st.error("SSN must be a number.")
