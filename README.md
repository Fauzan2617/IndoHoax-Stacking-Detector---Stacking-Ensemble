# 🚀 IndoHoax Stacking Detector

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![NLP](https://img.shields.io/badge/NLP-Sastrawi-green)
![Status](https://img.shields.io/badge/Status-Tugas%20Akhir-success)

Repositori ini berisi implementasi **Stacking Ensemble Learning** untuk mendeteksi berita hoaks berbahasa Indonesia menggunakan pendekatan Natural Language Processing (NLP).

---

## 📖 Latar Belakang
Model klasifikasi teks tunggal (seperti Naïve Bayes atau SVM) sering kali memiliki keterbatasan dalam menangkap kompleksitas data teks. Oleh karena itu, digunakan pendekatan **Stacking Ensemble Learning** untuk meningkatkan performa model dengan menggabungkan beberapa algoritma.

---

## ✨ Fitur Utama
- **Custom NLP Preprocessing Pipeline:** Pembersihan teks spesifik bahasa Indonesia
- **Dynamic Ensemble Architecture:** Modul pengujian otomatis untuk membandingkan model
- **Robustness Testing:** Pengujian model pada data bersih dan kotor
- **Modular Codebase:** Struktur kode terpisah seperti standar industri

---

## 🧠 Arsitektur Model
- **Level-0 (Base Learners):**
  - Multinomial Naïve Bayes (Probabilistik)
  - Support Vector Machine (Geometris)
  - Random Forest (Ensemble/Tree-based)
  - Logistic Regression (Statistik Linear)

- **Level-1 (Meta-Learner):**
  - Logistic Regression

- **Feature Extraction:**
  - TF-IDF (Term Frequency - Inverse Document Frequency)

---

## 📁 Struktur Repository
```text
TugasAkhir_Hoaks/
│
├── data/
│   ├── raw/              # Dataset asli (belum diproses)
│   ├── processed/        # Data teks bersih & Vector TF-IDF (.pkl)
│   └── models/           # Model Stacking final yang sudah dilatih
│
├── notebooks/            # Eksperimen & Analisis Data
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_eda_and_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
│
├── src/                  # Source code utama (Core Functions)
│   ├── preprocessor.py   # Modul pembersihan teks Sastrawi & Regex
│   └── utils.py          # Fungsi bantuan Pickle load/save
│
├── README.md             # Dokumentasi
└── requirements.txt      # Daftar dependensi


🛠️ Persyaratan Sistem & Instalasi
Pastikan kamu telah menginstal Python 3.10 atau versi yang lebih baru. Sangat disarankan menggunakan Virtual Environment.

1. Clone repositori ini:
git clone [https://github.com/username-kamu/IndoHoax-Stacking.git](https://github.com/username-kamu/IndoHoax-Stacking.git)
cd IndoHoax-Stacking

2. Buat dan aktifkan Virtual Environment:
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Instal dependensi:
pip install -r requirements.txt

📊 Alur Penggunaan (Reproducibility)
Untuk menjalankan ulang eksperimen dari awal hingga akhir, buka folder notebooks/ dan jalankan file secara berurutan:

1. Jalankan 01_data_preprocessing.ipynb untuk membersihkan teks dan melakukan Train-Test Split.
2. Jalankan 02_eda_and_feature_engineering.ipynb untuk pembobotan kata menggunakan TF-IDF.
3. Jalankan 03_model_training.ipynb untuk menguji kombinasi Stacking dan melatih model final.
4. Jalankan 04_model_evaluation.ipynb untuk melihat hasil evaluasi metrik (Akurasi, Presisi, Recall, F1-Score) pada skenario data bersih dan kotor.
