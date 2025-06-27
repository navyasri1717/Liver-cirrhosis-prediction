
      import streamlit as st
      import pandas as pd
      import numpy as np
      import joblib

      # Load trained model and normalizer
      model = joblib.load("model.pkl")
      normalizer = joblib.load("normalizer.pkl")

      # App title
      st.title("🩺 Liver Cirrhosis Prediction App")
      st.markdown("Enter the details below to predict if the person has liver cirrhosis.")

      # Input fields
      age = st.number_input("Age", min_value=1, max_value=120, step=1)
      bilirubin = st.number_input("Total Bilirubin", min_value=0.0, format="%.2f")
      alk_phosphate = st.number_input("Alkaline Phosphotase", min_value=0.0, format="%.2f")
      sgpt = st.number_input("SGPT (Alanine Aminotransferase)", min_value=0.0, format="%.2f")
      sgot = st.number_input("SGOT (Aspartate Aminotransferase)", min_value=0.0, format="%.2f")
      proteins = st.number_input("Total Proteins", min_value=0.0, format="%.2f")
      albumin = st.number_input("Albumin", min_value=0.0, format="%.2f")
      ratio = st.number_input("Albumin/Globulin Ratio", min_value=0.0, format="%.2f")

      # Prediction button
      if st.button("Predict"):
          input_data = np.array([[age, bilirubin, alk_phosphate, sgpt, sgot, proteins, albumin, ratio]])
          input_data_normalized = normalizer.transform(input_data)
          prediction = model.predict(input_data_normalized)

          if prediction[0] == 1:
              st.error("⚠ The model predicts that liver cirrhosis is likely.")
          else:
              st.success("✅ The model predicts that liver cirrhosis is not likely.")
      