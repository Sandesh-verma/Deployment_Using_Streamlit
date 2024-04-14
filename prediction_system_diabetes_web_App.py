# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 
import streamlit as st


loaded_model=pickle.load(open('C:/Users/sande/Desktop/weekends/Diabetes_Prediction_Model.sav','rb'))

def diabetes_prediction(input_values):

    input_numpy_array=np.array(input_values)

    input_reshaping=input_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_reshaping)

    print(prediction)

    if(prediction[0]==0):
        return 'Person is NOT Diabetic'
    else:
        return 'Person is Diabetic' 
        
def main():
    
    st.title('Diabetes Prediction Web App')
    								
    Pregnancies=st.text_input('No.of Pregnancies')
    Glucose=st.text_input('Glucose value')
    BloodPressure=st.text_input('BloodPressure value ')
    SkinThickness=st.text_input('SkinThickness value')
    Insulin=st.text_input('Insulin value')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    Age=st.text_input(' Age')
    
    diagnosis=''
    
    if st.button('Diabetes_test_results'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)


if __name__ == '__main__':
    main()
    
    