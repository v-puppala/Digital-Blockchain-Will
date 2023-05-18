
import streamlit as st
import http.client
import hashlib
from dataclasses import dataclass
import requests
from pathlib import Path
import os
from dotenv import load_dotenv
import json
from web3 import Web3
from pathlib import Path
from dataclasses import dataclass



# @dataclass
# class RealEstate:
#     name: str
#     ssn: str
#     dob: str
#     assetName: str
#     assetVal: int

#testing for presence of .env
ans=load_dotenv('.env')
print(ans)

#streamlit form for Date of birth user input
month = None
day = None
year = None
submit=False
dob='1/1/1910'
with st.form("dob_form"):
        st.write("Date of Birth:")
        day = st.number_input("Day", min_value=1, max_value=31, step=1)
        month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        year = st.number_input("Year", min_value=1910, max_value=2010, step=1)
        submitted = st.form_submit_button("Submit")
        if submitted:
            submit=True

dob=f'{month}/{day}/{year}'      


#sidebar single field userinputs

name=st.sidebar.text_input("what is your name")

ssn = st.sidebar.text_input("Enter your Social Security Number:", type="password")


#check if input meets length requirements
if ssn:
    if len(ssn) !=9:
        st.error("SSN must be 9 digits long.")
    if ssn.isdigit()==False:
        st.error("SSN must be a number.")

#enter ssn again for extra assurance
ssn_again=st.sidebar.text_input("Enter your Social Security Number Again:", type="password")


if ssn_again:
    if ssn!=ssn_again:
        st.error("SSNs don't match")
        
#For our new technology, and inspired by Gabe's question during the presentation today
#The new package/technology we're using is Cryptodome to encrypt the ssn into a private key
#with this extra layer of encryption, the ssn number will be represented as a ciphertext whose value is incredibly computationally difficult to decode


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX) #generate new cypher based on AES (Advanced encryption standard) sprecification
encoding=ssn.encode() #convert to byte code
ssn,public=cipher.encrypt_and_digest(encoding) #encrypt encoded data

# address input
address = st.sidebar.text_input("Enter your address")

# Display the entered address
st.write(address)

zip = st.sidebar.text_input("Enter your zipcode")

st.write(zip)

city = st.sidebar.text_input("Enter your city")

st.write(city)

state = st.sidebar.text_input("Enter your state")

st.write(state) 

asset_url=st.sidebar.text_input("Enter the URL for webpage displaying land asset") #note that this may need to be the Zillow specific URL--future versions will not be so restrictive
#future versions will not ask for url but rather be able to extrapolate this information from the customer simply providing property address

assetName=st.sidebar.text_input("Enter the name of your asset. ex: Johnson Estate, Dude Ranch etc.")


key=os.getenv("ALPACA_API_KEY")
url=os.getenv("WEB3_PROVIDER_URI")
#contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
contract_address="0xd9145CCE52D386f254917e481eB44e9943F39138"
w3 = Web3(Web3.HTTPProvider(url))
accounts=w3.eth.accounts

#give user option to choose their own digital wallet from dropdown menu
account = st.selectbox("Select Wallet", options=accounts)
#account=Web3.toChecksumAddress(account)

#note make sure abi file is in same directory
with open(Path('./TokenizedWill.json')) as f:
    property_abi = json.load(f)

#Create a ETH contract object that resides in local Ganache machine and is an instance of deployed Property Smart Contract
contract = w3.eth.contract(
        address=contract_address,
        abi=property_abi
)      

#if zillow api is available: 
assetVal=0
if key:
    #code below is from rapidAPI's deployment of the Zillow API: https://rapidapi.com/apimaker/api/zillow-com1/
    url = asset_url

    querystring = {"zpid":"2080998890"}

    headers = {
	    "X-RapidAPI-Key": key,
	    "X-RapidAPI-Host": "zillow-com1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data=response.json()
    assetVal=int(data['price'])
else:
    #if zillow api is not available, fair price appraisal is not gauranteed
    assetVal=st.sidebar.number_input("Enter the asset value:",step=1)
    
def register():
    hash=contract.functions.registerAsset(account,name,ssn,dob,assetName,assetVal,asset_url).transact({'from':account,'gas':1000000})
    receipt = w3.eth.waitForTransactionReceipt(hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    



#cont=st.button("Continue", disabled="ssn" not in st.session_state)
cont=st.button("Continue")
#cont_fulfill=False #Boolean for whetehr or not we should fulfil request once user presses continue button



if len(ssn)==9 and ssn.isdigit() and ssn_again==ssn:
    
    #enter this information into database
    #conn = "sqlite:///customer_database.db"
    #engine = sqlalchemy.create_engine(conn)

    st.session_state["ssn"]=ssn
    
else:
    st.sidebar.write('make sure your social security numbers are matching, are numeric, and are 9-digits')

if cont:
    if len(ssn)==9 or ssn.isdigit()==True and ssn_again==ssn and name and month and day and year and address and zip and submit and asset_url and assetName:
        #cont_fulfill=True #placeholder
        # st.session_state["name"]=name
        # st.session_state["month"]=month
        # st.session_state["day"]=day
        # st.session_state["year"]=year
        # st.session_state["address"]=address
        # st.session_state["zip"]=zip
        # st.session_state["submit"]=submit
        
        register()
        
    else:
        st.write('Make sure all fields are filled and filled to the specifications laid out')



# sampletoken=RealEstate(name="Vishal",ssn="1234567",assetName="house",dob="05/16/2023",assetVal=5)

# token=RealEstate(name=f'{name}',ssn=f'{ssn}',assetName="house",dob=f'{month}/{day}/{year}',assetVal=5)




