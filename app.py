# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:52:36 2023

@author: Aryan
Modified by AI to look professional.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration - must be the first Streamlit command
st.set_page_config(page_title="Trivedya Disease Detection", page_icon="⚕️", layout="wide")

# Custom CSS for professional look
st.markdown("""
<style>
    /* Styling the main container */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Custom button styling */
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        border: 2px solid #4CAF50;
        color: #4CAF50;
    }
    
    /* Result box styling */
    .success-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .error-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Headings */
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
    }
    h3 {
        color: #34495e;
    }
</style>
""", unsafe_allow_html=True)

# Loading the saved models
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("parkinsons_model.sav", 'rb'))

# Sidebar for navigation
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Trivedya System</h2>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    selected = option_menu('Disease Detection',
                          ['Diabetes Detection',
                           'Heart Disease Detection',
                           "Parkinson's Disease Detection"],
                          icons=['activity', 'heart', 'person'],
                          menu_icon="cast",
                          default_index=0,
                          styles={
                              "container": {"padding": "5!important", "background-color": "#fafafa"},
                              "icon": {"color": "#4CAF50", "font-size": "25px"}, 
                              "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                              "nav-link-selected": {"background-color": "#4CAF50"},
                          })
    
    st.markdown("<br><br><br><br><br><p style='text-align:center; color:grey; font-size:12px;'>Powered by Machine Learning</p>", unsafe_allow_html=True)


# Diabetes Prediction Page
if selected == 'Diabetes Detection':
    st.title('🩸 Diabetes Detection')
    st.markdown("Please enter the patient's medical details below to predict the likelihood of diabetes.")
    st.markdown("---")
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        SkinThickness = st.number_input('Skin Thickness value', min_value=0.0, step=1.0)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.01)
        
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0.0, step=1.0)
        Insulin = st.number_input('Insulin Level', min_value=0.0, step=1.0)
        Age = st.number_input('Age of the Person', min_value=0, step=1)
        
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0.0, step=1.0)
        BMI = st.number_input('BMI value', min_value=0.0, step=0.1)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Code for Prediction
    if st.button('Run Diabetes Test'):
        try:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if diab_prediction[0] == 1:
                st.markdown('<div class="error-box">⚠️ The person is diabetic</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">✅ The person is not diabetic</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# Heart Disease Prediction Page
if selected == 'Heart Disease Detection':
    st.title('❤️ Heart Disease Detection')
    st.markdown("Please enter the patient's medical details below to predict the likelihood of heart disease.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', min_value=0, step=1)
        trestbps = st.number_input('Resting Blood Pressure', min_value=0.0, step=1.0)
        restecg = st.number_input('Resting Electrocardiographic results', min_value=0.0, step=1.0)
        oldpeak = st.number_input('ST depression induced by exercise', step=0.1)
        thal = st.number_input('thal (0=normal; 1=fixed defect; 2=reversable)', min_value=0, max_value=2, step=1)
        
    with col2:
        sex = st.number_input('Sex (1=Male, 0=Female)', min_value=0, max_value=1, step=1)
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0.0, step=1.0)
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0.0, step=1.0)
        slope = st.number_input('Slope of the peak exercise ST segment', min_value=0.0, step=1.0)
        
    with col3:
        cp = st.number_input('Chest Pain types (0-3)', min_value=0, max_value=3, step=1)
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)', min_value=0, max_value=1, step=1)
        exang = st.number_input('Exercise Induced Angina (1=Yes, 0=No)', min_value=0, max_value=1, step=1)
        ca = st.number_input('Major vessels colored by flourosopy (0-3)', min_value=0, max_value=3, step=1)
        
    st.markdown("<br>", unsafe_allow_html=True)
     
    # Code for Prediction
    if st.button('Run Heart Disease Test'):
        try:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
            
            if heart_prediction[0] == 1:
                st.markdown('<div class="error-box">⚠️ The person is having heart disease</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">✅ The person does not have any heart disease</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
        
# Parkinson's Prediction Page
if selected == "Parkinson's Disease Detection":
    st.title("🧠 Parkinson's Disease Detection")
    st.markdown("Please enter the patient's voice measurement details below to predict the likelihood of Parkinson's disease.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', step=0.1)
        Jitter_percent = st.number_input('MDVP:Jitter(%)', step=0.001, format="%.5f")
        RAP = st.number_input('MDVP:RAP', step=0.001, format="%.5f")
        Shimmer = st.number_input('MDVP:Shimmer', step=0.001, format="%.5f")
        APQ3 = st.number_input('Shimmer:APQ3', step=0.001, format="%.5f")
        DDA = st.number_input('Shimmer:DDA', step=0.001, format="%.5f")
        RPDE = st.number_input('RPDE', step=0.001, format="%.5f")
        spread2 = st.number_input('spread2', step=0.001, format="%.5f")
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', step=0.1)
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', step=0.00001, format="%.6f")
        PPQ = st.number_input('MDVP:PPQ', step=0.001, format="%.5f")
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', step=0.01)
        APQ5 = st.number_input('Shimmer:APQ5', step=0.001, format="%.5f")
        NHR = st.number_input('NHR', step=0.001, format="%.5f")
        DFA = st.number_input('DFA', step=0.001, format="%.5f")
        D2 = st.number_input('D2', step=0.001, format="%.5f")
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', step=0.1)
        DDP = st.number_input('Jitter:DDP', step=0.001, format="%.5f")
        APQ = st.number_input('MDVP:APQ', step=0.001, format="%.5f")
        HNR = st.number_input('HNR', step=0.1)
        spread1 = st.number_input('spread1', step=0.001, format="%.5f")
        PPE = st.number_input('PPE', step=0.001, format="%.5f")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Code for Prediction    
    if st.button("Run Parkinson's Test"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])                          
            
            if parkinsons_prediction[0] == 1:
                st.markdown('<div class="error-box">⚠️ The person has Parkinson\'s disease</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">✅ The person does not have Parkinson\'s disease</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
