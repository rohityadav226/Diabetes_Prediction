import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import mysql.connector

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_diabetes(Gender, Age, Height, Weight, Waist, Hip, Glucose, Cholesterol, HDLChol, SystolicBP, DiastolicBP): 

    
    """Let's Predict Diabetes
    This is using docstrings for vitals.
    ---
    parameters:
      - name: Gender
        in: query
        type: number
        required: true
      - name: Age
        in: query
        type: number
        required: true
      - name: Height
        in: query
        type: number
        required: true
      - name: Weight
        in: query
        type: number
        required: true
      # - name: BMI
      #   in: query
      #   type: number
      #   required: true
      - name: Waist
        in: query
        type: number
        required: true
      - name: Hip
        in: query
        type: number
        required: true
      # - name: WaistbyHipRatio
      #   in: query
      #   type: number
      #   required: true
      - name: Glucose
        in: query
        type: number
        required: true
      - name: Cholesterol
        in: query
        type: number
        required: true
      - name: HDLChol
        in: query
        type: number
        required: true  
      - name: SystolicBP
        in: query
        type: number
        required: true 
      - name: DiastolicBP
        in: query
        type: number
        required: true   
    responses:
        200:
            description: The output values
        
    """
    db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='diabetes_data')
    mycursor=db.cursor()
    sql = "INSERT INTO patient_data(Gender, Age, Height, Weight, Waist, Hip, Glucose, Cholesterol, HDL_Cholesterol, Systolic_BP, Diastolic_BP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, (Gender, Age, Height, Weight, Waist, Hip, Glucose, Cholesterol, HDLChol, SystolicBP, DiastolicBP))
    db.commit()
    db.close()
    BMI = Weight*703/Height**2
    WaistbyHipRatio = Waist/Hip
    prediction=classifier.predict([[Gender, Age, Height, Weight, BMI, Waist, Hip, WaistbyHipRatio, Glucose, Cholesterol, HDLChol, SystolicBP, DiastolicBP]])
    # prob_0 = prediction[0][0]
    # prob_1 = prediction[0][1]
    # if prob_0>prob_1:
    #     return 'As per the model prediction you might not have diabetes'
    # else:
    #   return f'There is a {prob_1*100:.3f}% chance that you may have Diabetes'
    if prediction==0:
        return 'As per the model prediction you might not have diabetes'
    return 'As per the model prediction you might have diabetes. Please consult with your doctor'
	
def main():
    #st.title("Diabetes Prediction Using ML")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Diabetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender = st.text_input("Gender- 'Enter 1 for Male & 0 for Female'","")
    Age = st.text_input("Age","")
    Height = st.text_input("Height - in cm","")
    Weight = st.text_input("Weight - in pounds","")
    # BMI = st.text_input("BMI","")
    Waist = st.text_input("Waist - in inches","")
    Hip = st.text_input("Hip - in inches","")
    # WaistbyHipRatio = st.text_input("Waist/Hip Ratio","")
    Glucose = st.text_input("Glucose","")
    Cholesterol = st.text_input("Cholesterol","")
    HDLChol = st.text_input("HDL Cholesterol","")
    SystolicBP = st.text_input("Systolic BP","")
    DiastolicBP = st.text_input("Diastolic BP","")
    result=""
    if st.button("Predict"):
      # BMI = (float(Weight)*703)/(float(Height)**2)
      # WaistbyHipRatio = float(Waist)/float(Hip)
      result=predict_diabetes(float(Gender), float(Age), float(Height), float(Weight), float(Waist), float(Hip), float(Glucose), float(Cholesterol), float(HDLChol), float(SystolicBP), float(DiastolicBP))
    st.success(result)

if __name__=='__main__':
    main()
