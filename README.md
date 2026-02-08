# House_price_prediction_system
An end-to-end Machine Learning application that predicts house prices using structural features. The system includes data preprocessing, feature encoding, Random Forest model training, evaluation, and deployment with Streamlit. Users input house dimensions in meters, which are automatically converted to square feet for real-time price prediction.

# House Price Prediction System

A Machine Learning web application that predicts house prices based on house features such as area, number of bedrooms, bathrooms, parking space, and furnishing status.

## Project Overview

This project uses a Machine Learning model trained using Random Forest Regressor to estimate house prices. The model is deployed using Streamlit for interactive user input and real-time prediction.

## Features

- Predict house price instantly
- Input house size in meters (auto conversion to square feet)
- Interactive dashboard UI
- Machine Learning pipeline with preprocessing
- Real-time prediction

## Machine Learning Workflow

1. Data preprocessing using Scikit-learn Pipeline
2. Encoding categorical variables
3. Model training using Random Forest Regressor
4. Model evaluation using MAE and R² score
5. Model saved using Joblib
6. Deployment with Streamlit

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## Run Locally

```bash
streamlit run house_price_app.py

