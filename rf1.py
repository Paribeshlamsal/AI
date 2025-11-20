# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

st.set_page_config(page_title="Telco Customer Churn", layout="wide")

st.title("📊 Telco Customer Churn Prediction with Random Forest")

# -----------------------------
# Upload dataset
# -----------------------------
st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # -----------------------------
    # Data Cleaning
    # -----------------------------
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    if 'customerID' in df.columns:
        df.drop('customerID', axis=1, inplace=True)

    st.write("✅ Data Cleaning Done")

    # -----------------------------
    # Encoding categorical columns
    # -----------------------------
    cat_cols = df.select_dtypes(include=['object']).columns
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])

    st.write("✅ Encoding Completed")
    
    # -----------------------------
    # Split data
    # -----------------------------
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    test_size = st.sidebar.slider("Test size", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    st.write(f"✅ Data split into Train ({round((1-test_size)*100)}%) and Test ({round(test_size*100)}%)")

    # -----------------------------
    # Train Random Forest
    # -----------------------------
    n_estimators = st.sidebar.slider("Number of Trees", 50, 500, 200, 50)
    max_depth = st.sidebar.slider("Max Depth (0=None)", 0, 50, 0, 1)
    max_depth = None if max_depth==0 else max_depth

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        max_features='sqrt',
        min_samples_split=2,
        min_samples_leaf=1,
        bootstrap=True,
        oob_score=True,
        random_state=42
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.subheader("Model Evaluation")
    st.write(f"**Test Accuracy:** {accuracy_score(y_test, y_pred):.4f}")
    st.write(f"**OOB Score:** {model.oob_score_:.4f}")

    st.text("Classification Report:")
    st.text(classification_report(y_test, y_pred))

    # -----------------------------
    # Feature Importance
    # -----------------------------
    st.subheader("Feature Importance")
    importances = pd.Series(model.feature_importances_, index=X.columns)
    importances = importances.sort_values()

    fig, ax = plt.subplots(figsize=(10,6))
    importances.plot(kind='barh', ax=ax)
    plt.title("Feature Importance")
    st.pyplot(fig)

    # -----------------------------
    # Single Prediction
    # -----------------------------
    st.subheader("Predict Single Customer Churn")
    st.write("Enter feature values for a single customer below:")

    input_data = {}
    for col in X.columns:
        val = st.number_input(f"{col}", value=float(X[col].median()))
        input_data[col] = val

    if st.button("Predict Churn"):
        single_df = pd.DataFrame([input_data])
        pred = model.predict(single_df)[0]
        st.write(f"Predicted Churn: {'Yes' if pred==1 else 'No'}")
