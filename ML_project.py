import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset (Height, Weight, Intelligence Level)
@st.cache_data
def load_data():
    data = {
        "Height (cm)": [160, 170, 180, 50, 60, 70],  # Humans vs Animals
        "Weight (kg)": [60, 70, 80, 10, 20, 30],
        "Intelligence Level": [8, 9, 10, 2, 3, 4],  # Arbitrary scale
        "Category": [1, 1, 1, 0, 0, 0]  # 1 = Human, 0 = Animal
    }
    df = pd.DataFrame(data)
    return df

# Load dataset
df = load_data()

# Train model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df["Category"])

# Streamlit UI
st.title("🧑‍🤝‍🦊 Animal vs. Human Classifier")

st.sidebar.header("🔹 Enter Features")
height = st.sidebar.slider("Height (cm)", float(df["Height (cm)"].min()), float(df["Height (cm)"].max()))
weight = st.sidebar.slider("Weight (kg)", float(df["Weight (kg)"].min()), float(df["Weight (kg)"].max()))
intelligence = st.sidebar.slider("Intelligence Level (1-10)", float(df["Intelligence Level"].min()), float(df["Intelligence Level"].max()))

# Prediction
input_data = [[height, weight, intelligence]]
prediction = model.predict(input_data)
prediction_class = "Human" if prediction[0] == 1 else "Animal"

# Display Result
st.subheader("📌 Prediction Result =")
st.write(f"🔍 The predicted category is:= **{prediction_class}**")

st.write("This model uses a Random Forest Classifier trained on a small dataset to predict whether an entity is an **Animal or a Human**.")

# Display sample dataset
st.subheader("📊 Sample Dataset -")
st.dataframe(df)
