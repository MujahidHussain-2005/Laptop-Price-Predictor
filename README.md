# 💻 Laptop Price Predictor (End-to-End ML Project)

An interactive web application that predicts the market price of a laptop based on its hardware specifications. This project features a **FastAPI** backend and a **Streamlit** frontend.

---

## 🚀 Features
- **Accurate Predictions:** Uses a trained Machine Learning model (Random Forest/XGBoost) to estimate prices.
- **Dual-Layer Architecture:** 
  - **Backend:** FastAPI for high-performance model serving.
  - **Frontend:** Streamlit for a clean, user-friendly interface.
- **Comprehensive EDA:** Full data cleaning and exploration documented in Jupyter Notebook.

## 🛠️ Tech Stack
- **Languages:** Python
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
- **API:** FastAPI, Pydantic, Uvicorn
- **UI:** Streamlit
- **Serialization:** Pickle

---

## 📂 Project Structure
```text
├── data/
│   └── laptop_data.csv       # Dataset used for training
├── models/
│   └── pipe.pkl              # Serialized ML Pipeline
├── notebooks/
│   └── laptop_price.ipynb    # Data Analysis & Model Training
├── main.py                   # FastAPI Backend (API)
├── streamlitapp.py           # Streamlit Frontend (UI)
├── requirements.txt          # Project Dependencies
├── .gitignore                # Files to ignore in Git
└── README.md                 # Documentation

---

#  ⚙️ Installation & Setup
## 1. Clone the Repository
git clone https://github.com
cd laptop-price-predictor

## 2. Install Dependencies
pip install -r requirements.txt

## 3. Run the Backend (FastAPI)
uvicorn main:app --reload

## 4. Run the Frontend (Streamlit)
streamlit run streamlitapp.py

---
