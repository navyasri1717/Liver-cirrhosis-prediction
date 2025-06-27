
      import streamlit as st
      import pickle
      import numpy as np

      # Load the model
      with open("model.pkl", "rb") as f:
          model = pickle.load(f)

          # Load the scaler
          with open("normalizer.pkl", "rb") as f:
              scaler = pickle.load(f)

              st.set_page_config(page_title="Liver Cirrhosis Prediction", layout="centered")

              st.title("🧪 Liver Cirrhosis Prediction App")
              st.markdown("Predict whether a person is likely to have liver cirrhosis based on medical parameters.")

              # Input fields
              age = st.number_input("Age", min_value=1, max_value=120)
              gender = st.selectbox("Gender", ["Male", "Female"])
              total_bilirubin = st.number_input("Total Bilirubin (mg/dL)")
              direct_bilirubin = st.number_input("Direct Bilirubin (mg/dL)")
              alkaline_phosphotase = st.number_input("Alkaline Phosphotase (IU/L)")
              alamine_aminotransferase = st.number_input("Alamine Aminotransferase (IU/L)")
              aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase (IU/L)")
              total_proteins = st.number_input("Total Proteins (g/dL)")
              albumin = st.number_input("Albumin (g/dL)")
              ag_ratio = st.number_input("Albumin and Globulin Ratio")

              # Gender to numeric
              gender_num = 1 if gender == "Male" else 0

              # Predict button
              if st.button("Predict"):
                  input_data = np.array([[age, gender_num, total_bilirubin, direct_bilirubin,
                                              alkaline_phosphotase, alamine_aminotransferase,
                                                                          aspartate_aminotransferase, total_proteins,
                                                                                                      albumin, ag_ratio]])

                                                                                                          input_scaled = scaler.transform(input_data)
                                                                                                              prediction = model.predict(input_scaled)

                                                                                                                  if prediction[0] == 1:
                                                                                                                          st.error("⚠️ High Risk: Liver Cirrhosis Likely")
                                                                                                                              else:
                                                                                                                                      st.success("✅ Low Risk: No Liver Cirrhosis Detected")
                                                                                                                                      