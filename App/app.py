import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn



model = pickle.load(open("Loan_prediction.sav", "rb"))
df = pickle.load(open("df.sav","rb"))

st.image( "loan_img.PNG")


######################################################################################

dep = st.selectbox("Dependents",sorted(df["Dependents"].unique()))
ed = st.selectbox("Education",["Graduate","Not Graduate"])

if ed == "Not Graduate":
    ed = 0
else :
    ed = 1

se = st.selectbox("Self_Employed",["Yes","No"])

if se == "Yes":
    se = 1
else:
    se = 0
    
ae = st.number_input("ApplicantIncome (thousands)")

cai = st.number_input("Coapplicant income (thousands)")

la = st.number_input("Loan Amount (thousands)")

lat = st.selectbox("Loan Terms  (months) ", sorted(df["Loan_Amount_Term"].unique()))

ch = st.selectbox("Credit History",["Yes","No"])

if ch == "Yes":
    ch = 1
else:
    ch = 0

pa = st.selectbox("Property Area",["Urban","Rural","Semiurban"])

if pa == "Rural":
    pa = 0
elif pa == "Urban":
    pa = 1
else:
    pa = 2

# to create gap between to code
st.title("")

Loan_Prediction = ""

if st.button("Loan Prediction"):
    Loan_Prediction = model.predict([[dep, ed, se, ae, cai, la, lat, ch, pa]])
    
    if Loan_Prediction == 1:
        st.success('Loan has been Approved')
        st.image("loan_approved.jpg")
    else:
        st.error("Loan has been Rejected")
        st.image("loan_rejected.jpg")

# to create gap between to code
st.title("")
st.title("")

######################################################################################

self_massage = """Hi, I'm **Lalit Mahale**, I have done My Post Graduate Diploma in Artificial Intelligence in Artificial Intelligent from CDAC (act's) Pune """
git = "For see read and download code plz visite my github link \n **https://github.com/LalitMahale/Loan-Prediction.git**"
lin = "Follow at Linkdin - **https://www.linkedin.com/in/lalitmahale1997**"
email = "Email - **mahalelalit45@gmail.com**"

menu = st.sidebar.selectbox("About Section ",["","About Developer", "About Dataset","Social Media Links","Contact us"])

if menu == "":
    pass


elif  (menu == "About Developer") :
    st.image("developer.jpg")
    st.title("Developer ")
    st.header(self_massage)

    
elif (menu == "About Dataset"):
    st.image("OIP.jpg")
    st.title("Dataset ")
    st.write("Please for dataset Visit at Github link which is given in Social Media Links")

elif (menu == "Social Media Links"):
    st.image("social media.PNG")
    st.title("Social media Links ")
    st.write(git)
    st.write(lin)
    st.write(email)
    
elif menu == "Contact us":
    st.image("contact us.jpg")
    st.title("Email ID ")
    st.write(email)

st.image("home.jpg")

rad = st.radio("Navigation",["Home","About Developer","Contact us","Help"])

if rad == "About Developer":
    st.image("developer.jpg")
    st.title("Developer ")
    st.write(self_massage)
elif rad== "Home":
    st.header("Thanks For Vising ...")
    
elif rad == "Contact us":
    st.image("contact us.jpg")
    st.title("Email ID ")
    st.write(email)

# Description of Dataset
elif rad == "Help":
    data = {"Variable" : ["Dependents","Education","Self Employed","Applicant Income","Coapplicant Income","Loan amount",
                    "Loan Amount Term","Credit History","Property Area"],
    "Description ": ["Number of dependents","Applicant Education (Graduate/ Under Graduate)","	Self employed (Y/N)",
                   "Applicant income","Coapplicant income","Loan amount in thousands","Term of loan in months",
                   "credit history meets guidelines","Urban/ Semi Urban/ Rural"]}
    df = pd.DataFrame(data)
    st.table(df)