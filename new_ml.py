import streamlit as st
import pandas as pd
import pickle

xgb_model=pickle.load(open("xgb_model.sav","rb"))
st.title("Used car price prediction")
brand=st.selectbox(
    "Brand",
    ("Audi","BMW","Bentley","Chevrolet","Datsun","Fiat","Force","Ford","Honda","Hyundai","Isuzu","Jaguar","Jeep","Kia","Land","Lexus","MG","Mahindra","Maruti","Maserati","Mercedes-Benz","Mini","Mitibushi","Nissan","Porsche","Premier","Renault","Skoda","Tata","Toyata","Volkswagen")
)
kms_driven = st.number_input("KMS driven", min_value=0, max_value=None, step=1)

fuel=st.radio("Fuel",("Petrol","Diesel","Electric","LPG","CNG"))
transmission=st.radio("Transmission type",("Manual","Automatic"))



if transmission=="Mannual":
    transmission=0
else:
    transmission=1
ownership = st.number_input("Fuel (Ownership)", value=0.0, step=1.0, format="%.0f")

age=st.number_input("Age")
engine=st.number_input("Engine")
seats=st.number_input("Seats")

start=st.button("Predict")
if start:
    d= {
        'Audi': 0,
        'BMW' : 0,
        'Bentley':0,
        'Chevrolet':0,
        "Datsun" : 0,
        "Fiat" : 0,
        "Force" : 0,
        "Ford" : 0,
        "Honda" : 0,
        "Hyundai" : 0,
        "Isuzu" : 0,
        "Jaguar" : 0,
        "Jeep" : 0,
        "Kia" : 0,
        "Land" : 0,
        "Lexus" : 0,
        "MG" : 0,
        "Mahindra" : 0,
        "Maruti" : 0,
        "Maserati" :0,
        "Mercedes-Benz" :0,
        "Mini":0,
        "Mitsubishi":0,
        "Nissan":0,
        "Porsche":0,
        "Premier":0,
        "Renault":0,
        "Skoda":0,
        "Tata":0,
        "Toyata":0,
        "Volkswagen":0,
        "kms_driven":0,
        "transmission":0,
        "ownership": 0,
        "manufacture":0,
        "engine" :0 ,
        "Seats" : 0,
        "Cng" : 0,
        "Diesel" : 0,
        "Electric" : 0,
        "Lpg" : 0,
        }
    if brand in d:
        d[brand]=1
    if fuel in d:
        d[fuel]=1
    d["kms_driven"]=kms_driven
    d["transmission"]=transmission
    d["ownership"]=ownership
    d["engine"]=engine
    d["manufacture"]=age
    d["Seats"]=seats

    df= pd.DataFrame(columns=d.keys())
    df= df.append(d, ignore_index = True)

    xgb_pred=xgb_model.predict(df)[0]
    xgb_pred= round(xgb_pred)

    st.text(f"Your car would go for: {xgb_pred} [Predicted using xgb regression]")

