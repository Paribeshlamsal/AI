import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# -----------------------------
# Load and Train Model
# -----------------------------
@st.cache_data
def load_and_train():
    data = pd.read_csv(r"C:\Users\ACER\Desktop\AI\projects\data\USA_Housing.csv")

    # Features and target
    X = data[[
        'Avg. Area Income',
        'Avg. Area House Age',
        'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms',
        'Area Population'
    ]]
    y = data['Price']

    # Train-Test Split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Normalize
    scaler = StandardScaler()
    X_train_norm = scaler.fit_transform(X_train)
    X_val_norm = scaler.transform(X_val)

    # Train model
    model = LinearRegression()
    model.fit(X_train_norm, y_train)

    # Validation
    y_val_pred = model.predict(X_val_norm)
    rmse = np.sqrt(mean_squared_error(y_val, y_val_pred))

    return model, scaler, rmse

model, scaler, rmse = load_and_train()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🏡 USA Housing Price Prediction")
st.write("Enter house details to predict the price.")

# User Inputs
income = st.number_input("Average Area Income", min_value=10000, max_value=200000, value=65000, step=1000)
age = st.slider("Average Area House Age", 0, 20, 5)
rooms = st.slider("Average Area Number of Rooms", 1, 15, 6)
bedrooms = st.slider("Average Area Number of Bedrooms", 1, 10, 3)
population = st.number_input("Area Population", min_value=1000, max_value=80000, value=30000, step=1000)

# Prediction
if st.button("Predict Price"):
    new_house = np.array([[income, age, rooms, bedrooms, population]])
    new_house_norm = scaler.transform(new_house)
    price = model.predict(new_house_norm)[0]
    st.success(f"🏠 Predicted Price: ${price:,.2f}")

# Show model performance
st.write(f"📊 Model Validation RMSE: ${rmse:,.2f}")
