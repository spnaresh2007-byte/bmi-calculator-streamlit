import streamlit as st
import pandas as pd

st.title("BMI calculator")
name=st.text_input("Name")
age=st.number_input("Age")
weight=st.number_input("weight(kg)")
height=st.number_input("Height(M)")
gender=st.selectbox("Gender",["Male","Female"])
if weight==0:
    st.write("Weight cannot be zero")
if st.button("calculate"):
    bmi=(weight)/(height)**2
    st.write("BMI",bmi)        
    df=pd.DataFrame({
        "Name":[name],
        "Age":[age],
        "Weight":[weight],
        "Height":[height],
        "Gender":[gender],
        "Bmi":[bmi]})
    if bmi<18.5:
        st.write("under weight")
    elif bmi<24.9:
        st.write("normal")
    elif bmi<30:
        st.write("over weight")
    else:
        st.write("obese")

    df.to_csv("bmi.csv", index=False)
