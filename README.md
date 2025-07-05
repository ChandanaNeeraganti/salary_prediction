# salary_prediction
This system estimates an employee's future salary based on three key inputs: years of experience, annual increment rate, and current base salary. By analyzing these factors, it provides an accurate projection of future earnings, assisting individuals and organizations in salary planning and decision-making.

# 💼 Salary Predictor App

An interactive machine learning web app that predicts salary based on years of experience using Linear, Polynomial, or Custom formulas.

✅ Built with **Streamlit**  
📊 Powered by **Scikit-Learn**, **Pandas**, and **Matplotlib**  
📁 Includes both **single input** and **CSV bulk upload** features  

## 📌 Features

- 🔢 Predict salary from user-entered years of experience
- 📈 Choose between Linear, Polynomial, or Custom formula
- 📁 Upload a CSV file to run bulk salary predictions
- 🎨 Clean UI with selectable themes
- 💬 Takes slope (m) and intercept (c) from user for custom prediction

## 🚀 Live App

Try the app here 👉 [Streamlit Cloud Deployment](https://salaryprediction-er5qfsq3wdptb4zvkw2gzs.streamlit.app)


## 🧠 Machine Learning Model

- **Linear Regression** for modeling experience vs. salary
- **Polynomial Regression** (degree = 2) for improved curve fitting
- **Custom formula**: `Salary = m × Experience + c` based on user input

## 🛠️ Technologies Used

- `Streamlit` – UI
- `scikit-learn` – ML models
- `pandas` – Data handling
- `matplotlib` – Visualization

## 📁 Folder Structure
<pre> <code> ## 📁 Folder Structure ``` salary_prediction/ ├── app.py ├── requirements.txt ├── experience_salary.csv ├── README.md └── .streamlit/ └── config.toml ``` </code> </pre>





