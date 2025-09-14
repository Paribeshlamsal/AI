import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Load model and columns
# ------------------------------
model = joblib.load("titanic_model.pkl")
columns = joblib.load("titanic_columns.pkl")

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="wide"
)

# ------------------------------
# App Header with Titanic Image
# ------------------------------
st.markdown("""
<div style="text-align:center">
    <h1 style="color:#004080">🚢 Titanic Survival Prediction</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg" width="600">
    <p style="font-size:18px; color:#003366;">Predict whether a passenger would survive the Titanic disaster.</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# Sidebar Inputs
# ------------------------------
st.sidebar.header("Passenger Details")
pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
sex = st.sidebar.selectbox("Sex", ["male", "female"])
age = st.sidebar.slider("Age", 0, 100, 30)
fare = st.sidebar.slider("Fare", 0.0, 500.0, 20.0, step=0.1)
embarked = st.sidebar.selectbox("Port of Embarkation", ["C", "Q", "S"])

# ------------------------------
# Encode categorical inputs
# ------------------------------
sex = 0 if sex == "male" else 1
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_map[embarked]

# ------------------------------
# Prepare DataFrame for prediction
# ------------------------------
input_data = pd.DataFrame([{
    "Pclass": pclass,
    "Sex": sex,
    "Age": age,
    "Fare": fare,
    "Embarked": embarked
}])

input_data = input_data[columns]

# ------------------------------
# Prediction Button
# ------------------------------
if st.button("Predict Survival"):
    prediction = model.predict(input_data)[0]
    prediction_prob = model.predict_proba(input_data)[0][1]

    # Color combinations
    if prediction == 1:
        card_color = "#d0f0c0"  # light green
        text_color = "#006400"  # dark green
        emoji = "✅ SURVIVE"
    else:
        card_color = "#f8d7da"  # light red
        text_color = "#721c24"  # dark red
        emoji = "❌ NOT SURVIVE"

    # Display result card with Titanic image background
    st.markdown(f"""
    <div style="
        background-color:{card_color};
        padding:25px;
        border-radius:15px;
        text-align:center;
        border:2px solid {text_color};
        ">
        <h2 style="color:{text_color};">{emoji}</h2>
        <p style="font-size:20px; color:{text_color};">
        Survival Probability: <b>{prediction_prob*100:.2f}%</b>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("""
<p style="text-align:center; color:#004080; font-size:16px;">
Made with ❤️ using Python, Scikit-learn & Streamlit
</p>
""", unsafe_allow_html=True)
