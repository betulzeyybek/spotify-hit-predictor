
import streamlit as st
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

st.title("🎧 Spotify Şarkı Başarı Tahmini")
st.write("Aşağıdaki şarkı özelliklerini girerek hit olup olmayacağını tahmin edebilirsin!")

danceability = st.slider("Danceability (0.0 - 1.0)", 0.0, 1.0, 0.5)
loudness = st.slider("Loudness (dB)", -60.0, 0.0, -10.0)
speechiness = st.slider("Speechiness", 0.0, 1.0, 0.05)
acousticness = st.slider("Acousticness", 0.0, 1.0, 0.2)
instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.1)
valence = st.slider("Valence (0.0 - 1.0)", 0.0, 1.0, 0.5)
duration_ms = st.number_input("Duration (ms)", min_value=10000, max_value=1000000, value=200000)
time_signature = st.number_input("Time Signature", min_value=1, max_value=7, value=4)
chorus_hit = st.number_input("Chorus Hit Time (ms)", min_value=0, max_value=1000000, value=30000)
sections = st.number_input("Number of Sections", min_value=1, max_value=100, value=10)

features = np.array([[danceability, loudness, speechiness, acousticness,
                      instrumentalness, valence, duration_ms,
                      time_signature, chorus_hit, sections]])

df = pd.read_csv("dataset-of-10s.csv")
df = df.drop(["track", "artist", "uri"], axis=1)
X = df.drop("target", axis=1)
y = df["target"]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled[:, [0, 2, 3, 6, 9, 10, 11, 12, 13, 14]], y)

features_scaled = scaler.transform(np.concatenate([features, np.zeros((1, X.shape[1] - features.shape[1]))], axis=1))[:, [0, 2, 3, 6, 9, 10, 11, 12, 13, 14]]

if st.button("🎶 Tahmin Et"):
    prediction = model.predict(features_scaled)[0]
    if prediction == 1:
        st.success("✅ Bu şarkı muhtemelen bir HIT olacak!")
    else:
        st.warning("❌ Bu şarkı muhtemelen flop olabilir...")
