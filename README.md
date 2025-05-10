# 🎧 Spotify Şarkı Başarı Tahmini

Bu proje, Spotify şarkılarının ses özelliklerine göre **"Hit olur mu, flop mu?"** sorusuna makine öğrenmesiyle cevap arar.  
Kullanıcıdan alınan ses parametreleriyle tahmin yapan bir **Streamlit uygulaması** geliştirilmiştir.

---

## 🔍 Kullanılan Veri Seti
- Kaynak: [Spotify Hit Predictor Dataset - Kaggle](https://www.kaggle.com/datasets/theoverman/the-spotify-hit-predictor-dataset)
- İçerik: 2000’ler ve 2010’lara ait şarkıların dans edilebilirlik, enerji, akustiklik, valence gibi ses özellikleri
- Hedef: `target` sütunu (1 = Hit, 0 = Flop)

---

## 🧠 Kullanılan Modeller
- Logistic Regression ✅ *(en iyi performansı verdi)*
- KNN
- Decision Tree
- Naive Bayes

---

## ⚙️ Kullanılan Özellik Seçim Teknikleri
- SelectKBest
- PCA (Principal Component Analysis)
- RFE (Recursive Feature Elimination)

---

## 💻 Uygulama Özellikleri
- Kullanıcı arayüzü: Streamlit
- Gerçek zamanlı tahmin
- Türkçe destekli kullanıcı arayüzü
- Tamamen açık kaynak ve çalışır durumda

---

## 🚀 Uygulamayı Deneyin!

📎 **Canlı Uygulama Linki:**  
👉 [https://betul-hit-check.streamlit.app](https://betul-hit-check.streamlit.app)

---

## 📸 Ekran Görüntüsü

![Demo](ekran-goruntusu.png) <!-- (Eğer screenshot koyarsan depoya) -->

---

## 👩‍💻 Geliştiren
**Betül Zeybek**  
İstanbul Sabahattin Zaim Üniversitesi – Bilgisayar Mühendisliği  
Ders: Makine Öğrenmesi ve Uygulamaları  
Yıl: 2025

---

## 📂 Nasıl Çalıştırılır?

```bash
pip install -r requirements.txt
streamlit run app.py
