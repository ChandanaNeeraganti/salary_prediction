import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Load training data
df = pd.read_csv("experience_salary.csv")
X = df[["YearsExperience"]]
y = df["Salary"]

# App title
st.set_page_config(page_title="Salary Predictor", layout="centered")
st.title("💼 Salary Predictor")
st.write("Choose a model type and enter your experience to get the predicted salary.")

# Model selection
model_type = st.selectbox(
    "Choose Model", ["Linear Regression", "Polynomial Regression", "From User"]
)

# Initialize model or custom inputs
m = c = None

if model_type == "Linear Regression":
    model = LinearRegression()
    model.fit(X, y)

elif model_type == "Polynomial Regression":
    model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
    model.fit(X, y)

elif model_type == "From User":
    st.markdown("### ✍️ Enter increment money per year and startng salary")
    m = st.number_input("Increment per Year (m)", value=5000.0, step=500.0)
    c = st.number_input("starting Salary (c) (base salary)", value=30000.0, step=1000.0)

# ===============================
# 🎯 Single Experience Prediction
# ===============================
st.markdown("## 🎯 Predict for One Person")
experience = st.number_input("Years of Experience", min_value=0.0, step=0.1)

if st.button("Predict Salary"):
    if model_type == "From User":
        salary = m * experience + c
    else:
        salary = model.predict([[experience]])[0]

    st.success(f"💰 Estimated Salary: ₹{salary:,.2f}")

# =====================
# 📈 Optional Plot
# =====================


# ============================
# 📁 Bulk CSV Prediction
# ============================
st.write("---")
st.subheader("📁 Upload CSV for Bulk Predictions")

uploaded_file = st.file_uploader(
    "Upload a CSV file with a 'YearsExperience' column", type=["csv"]
)

if uploaded_file is not None:
    try:
        bulk_data = pd.read_csv(uploaded_file)

        if "YearsExperience" not in bulk_data.columns:
            st.error("❌ CSV must contain a 'YearsExperience' column.")
        else:
            st.success("✅ File uploaded successfully!")

            # If Custom Formula, ask again for CSV input m & c
            if model_type == "From User":
                st.markdown(
                    "### 🧮 Enter increment and starting salary for CSV Prediction"
                )
                m_csv = st.number_input(
                    "Increment per Year (m) for CSV", value=m, step=500.0
                )
                c_csv = st.number_input("Base Salary (c) for CSV", value=c, step=1000.0)

            if st.button("📊 Predict for Uploaded CSV"):
                if model_type == "From User":
                    bulk_data["Predicted Salary"] = bulk_data["YearsExperience"].apply(
                        lambda x: m_csv * x + c_csv
                    )
                else:
                    bulk_data["Predicted Salary"] = model.predict(
                        bulk_data[["YearsExperience"]]
                    )

                st.write("### 📋 Prediction Results")
                st.dataframe(bulk_data)

                # Download predicted results
                csv = bulk_data.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📥 Download Results as CSV",
                    data=csv,
                    file_name="salary_predictions.csv",
                    mime="text/csv",
                )

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
