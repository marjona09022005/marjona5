import streamlit as st
import pickle
import numpy as np

model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

bio_features = [
   "Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","DiabetesPedigreeFunction" ,"Age", "BMI"
]

result_mapping = {
   0: "Donor (Sog'lom)",
1: "Gepatit (Qandli diabetga uchrash)",
2: "Fibroz (Qandli diabetning oshib ketishi)",
3: "Sirroz (Qandli diabet pasayishi)",
4: "Donor gumon qilinmoqda (Kasallik ehtimoli)",
}

st.title("Qandli diabet Kasalligi tashxisi")

age = st.number_input("Yoshni kiriting", min_value=1, max_value=100, value=25, step=1)
sex = st.radio("Jinsni tanlang", options=["Erkak", "Ayol"])
sex_value = 1 if sex == "Erkak" else 0



inputs = []
for feature in bio_features:
    value = st.number_input(f"{feature}", value=0.0, step=0.1)
    inputs.append(value)

user_data = [age, sex_value] + inputs


if st.button("Natijani ko'rish"):
    prediction = model.predict([user_data])
    result = result_mapping.get(prediction[0], "Aniqlab bo'lmadi")
    st.success(f"Bashorat: {result}")



