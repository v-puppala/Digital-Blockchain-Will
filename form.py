
import streamlit as st
#import sqlalchemy
#from sqlalchemy import Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
import hashlib

#input field

# Base = declarative_base()

# class SomeClass(Base):
#     __tablename__ = 'Clients'
#     id = Column(Integer, primary_key=True) #this is the ssn
#     name =  Column(String(50))


ssn = st.sidebar.text_input("Enter your Social Security Number:", type="password")

#check if input meets length requirements
if ssn:
    if len(ssn) !=9:
        st.error("SSN must be 9 digits long.")
    if ssn.isdigit()==False:
        st.error("SSN must be a number.")

ssn_again=st.sidebar.text_input("Enter your Social Security Number Again:", type="password")

if ssn_again:
    if ssn!=ssn_again:
        st.error("SSNs don't match")

# Create a sidebar text box for address input
address = st.sidebar.text_input("Enter your address")

# Display the entered address
st.write(address)

zip = st.sidebar.text_input("Enter your zipcode")

st.write(zip)

city = st.sidebar.text_input("Enter your city")

st.write(city)

state = st.sidebar.text_input("Enter your state")

st.write(state) 


#cont=st.button("Continue", disabled="ssn" not in st.session_state)
cont=st.button("Continue")



if len(ssn)==9 and ssn.isdigit() and ssn_again==ssn:
    
    #enter this information into database
    #conn = "sqlite:///customer_database.db"
    #engine = sqlalchemy.create_engine(conn)

    st.session_state["ssn"]=ssn
    
else:
    st.write('make sure your social security numbers are matching, are numeric, and are 9-digits')
cont=st.button("Continue")
if cont and len(ssn)==9 and ssn.isdigit() and ssn_again==ssn:
    st.write('check the error messages and fix the errors')

@dataclass
class RealEstate:
    name: str
    ssn: str
    dob: str
    assetName: str
    AssetVal: int
token=RealEstate(name="Vishal",ssn="1234567",assetName="house",dob="05/16/2023",AssetVal=5)