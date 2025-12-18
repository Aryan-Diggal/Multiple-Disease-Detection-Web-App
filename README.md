# Trivedya Multiple Disease Detection System

Welcome to the **Trivedya Multiple Disease Detection System**! This web application leverages Machine Learning models to predict the likelihood of three major diseases based on patient medical data:
1. **Diabetes**
2. **Heart Disease**
3. **Parkinson's Disease**

## 🚀 Features
- **Interactive UI**: Built with Streamlit for a clean, user-friendly interface.
- **Accurate Predictions**: Uses pre-trained Machine Learning models (Support Vector Machine, Random Forest, etc.) to analyze user input.
- **Real-time Results**: Get instant feedback based on the medical parameters entered.

## 🛠️ Technology Stack
- **Python 3.x**
- **Streamlit**: Web application framework
- **Scikit-Learn**: Machine Learning library
- **Numpy & Pandas**: Data manipulation

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Aryan-Diggal/Multiple-Disease-Detection-Web-App.git
   cd Multiple-Disease-Detection-Web-App
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python -m streamlit run app.py
   ```

## 🧠 How it Works
1. Select the disease you want to test for from the sidebar menu.
2. Input the patient's medical details in the provided fields.
3. Click the "Run Test" button.
4. The system will process the input through the respective saved `.sav` model and display whether the person is at risk.

## 📝 License
This project is open-source and available for educational and research purposes.
