import streamlit as st
import pandas as pd
import joblib

# Load model
#model = joblib.load("house_price_model.pkl")
model_path = r"C:\Users\LENOVO\Desktop\House_price\house_price_model.pkl"
model = joblib.load(model_path)

# Page config
st.set_page_config(page_title="House Price Prediction", layout="wide")

# Header
st.title("🏠 House Price Prediction Dashboard")
st.markdown("Predict house prices using Machine Learning")

st.divider()

# Layout columns
col1, col2 = st.columns([1,1])

# ---------- INPUT PANEL ----------
with col1:
    st.subheader("House Details")

    st.markdown("### House Size")
    length = st.number_input("Length (meters)", min_value=1.0, value=40.0)
    width = st.number_input("Width (meters)", min_value=1.0, value=20.0)

    area = length * width * 10.764
    st.info(f"Calculated Area: {area:.2f} sq ft")

    bedrooms = st.number_input("Bedrooms", 1, 10, 4)
    bathrooms = st.number_input("Bathrooms", 1, 10, 2)
    stories = st.number_input("Stories", 1, 5, 3)

    mainroad = st.selectbox("Mainroad", ["yes", "no"])
    guest_room = st.selectbox("Guest Room", ["yes", "no"])
    basement = st.selectbox("Basement", ["yes", "no"])
    hotwater_heating = st.selectbox("Hotwater Heating", ["yes", "no"])
    airconditioning = st.selectbox("Airconditioning", ["yes", "no"])
    parking = st.number_input("Parking", 0, 5, 2)
    pref_area = st.selectbox("Preferred Area", ["yes", "no"])
    furnishing_status = st.selectbox(
        "Furnishing Status",
        ["furnished", "semi-furnished", "unfurnished"]
    )

    predict_button = st.button("Predict Price")

# ---------- RESULT PANEL ----------
with col2:
    st.subheader("Prediction Result")

    if predict_button:

        input_data = pd.DataFrame([{
            "Area": area,
            "Bedrooms": bedrooms,
            "Bathrooms": bathrooms,
            "Stories": stories,
            "Mainroad": mainroad,
            "Guest_room": guest_room,
            "Basement": basement,
            "Hotwater_heating": hotwater_heating,
            "Airconditioning": airconditioning,
            "Parking": parking,
            "Pref_area": pref_area,
            "Furnishing_status": furnishing_status
        }])

        prediction = model.predict(input_data)

        st.success(f"Predicted Price: ₦{prediction[0]:,.0f}")

        # Simple insight
        if area > 6000:
            st.write("✅ Large area significantly increased price.")
        elif area < 2000:
            st.write("ℹ️ Smaller area reduced the predicted price.")
