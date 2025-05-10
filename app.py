import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(page_title="Spotify Şarkı Başarı Tahmini", page_icon="🎧", layout="centered")

st.title("🎧 Spotify Şarkı Başarı Tahmini")
st.markdown("Aşağıdaki şarkı özelliklerini girerek **hit olup olmayacağını** tahmin edebilirsin!")

# Girişler (Kullanıcıdan alınan veriler)
danceability = st.slider("Dans Edilebilirlik (0.0 - 1.0)", 0.0, 1.0, 0.5)
loudness = st.slider("Ses Seviyesi (dB)", -60.0, 0.0, -10.0)
speechiness = st.slider("Konuşma Oranı (Speechiness)", 0.0, 1.0, 0.05)
acousticness = st.slider("Akustiklik (Acousticness)", 0.0, 1.0, 0.2)
instrumentalness = st.slider("Enstrümantal Oran (Instrumentalness)", 0.0, 1.0, 0.1)
valence = st.slider("Pozitiflik (Valence)", 0.0, 1.0, 0.5)
duration_ms = st.number_input("Şarkı Süresi (milisaniye)", min_value=10000, max_value=1000000, value=200000)
time_signature = st.number_input("Zaman İmzası (Time Signature)", min_value=1, max_value=7, value=4)
chorus_hit = st.number_input("Nakarat Başlangıcı (ms)", min_value=0, max_value=1000000, value=30000)
sections = st.number_input("Bölüm Sayısı", min_value=1, max_value=100, value=10)

# Özellik vektörü
features = np.array([[danceability, loudness, speechiness, acousticness,
                      instrumentalness, valence, duration_ms,
                      time_signature, chorus_hit, sections]])

# Model eğitimi
df = pd.read_csv("dataset-of-10s.csv")
df = df.drop(["track", "artist", "uri"], axis=1)
X = df.drop("target", axis=1)
y = df["target"]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled[:, [0, 2, 3, 6, 9, 10, 11, 12, 13, 14]], y)

# Giriş verisini ölçekle
features_scaled = scaler.transform(
    np.concatenate([features, np.zeros((1, X.shape[1] - features.shape[1]))], axis=1)
)[:, [0, 2, 3, 6, 9, 10, 11, 12, 13, 14]]

# Tahmin
if st.button("🎶 Tahmin Et"):
    prediction = model.predict(features_scaled)[0]
    proba = model.predict_proba(features_scaled)[0][1]  # Hit olma olasılığı

    if prediction == 1:
        st.success("✅ Bu şarkı büyük ihtimalle bir **HIT** olacak!")
    else:
        st.warning("❌ Bu şarkı muhtemelen **hit olmayabilir...**")

    st.info(f"📊 Hit olma olasılığı: **%{proba*100:.2f}**")
