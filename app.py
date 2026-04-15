import streamlit as st
import time
import pandas as pd
from src.utils import load_objek
from src.preprocessor import bersihkan_teks_minimal  # 🔥 GANTI KE MINIMAL

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Deteksi Hoaks | Stacking Ensemble",
    page_icon="🕵️‍♂️",
    layout="centered"
)

# --- 2. LOAD MODEL (CACHE) ---
@st.cache_resource
def load_sistem():
    try:
        data_vektor = load_objek('data/processed/data_vektor.pkl')
        tfidf_vectorizer = data_vektor['vectorizer']
        model_stacking = load_objek('models/stacking_final.pkl')
        return tfidf_vectorizer, model_stacking
    except Exception as e:
        st.error(f"Gagal memuat model. Error: {e}")
        return None, None

# --- 3. HEADER ---
st.title("🕵️‍♂️ Sistem Deteksi Berita Hoaks")
st.markdown("""
Aplikasi ini memprediksi kebenaran sebuah berita berbahasa Indonesia menggunakan metode 
**Stacking Ensemble Learning**.
""")
st.divider()

# Load model
vectorizer, model = load_sistem()

if vectorizer and model:

    # --- 4. INPUT ---
    st.subheader("Uji Berita Baru")

    teks_input = st.text_area(
        "Masukkan narasi berita atau teks cuitan Twitter di bawah ini:",
        height=150,
        placeholder="Ketik teks berita di sini..."
    )

    if st.button("🔍 Deteksi Sekarang", type="primary"):

        if len(teks_input.strip()) < 10:
            st.warning("⚠️ Teks terlalu pendek!")
        else:
            with st.spinner("Menganalisis teks..."):
                time.sleep(1)

                # --- PROSES ML ---
                # 🔥 1. Preprocessing MINIMAL (biar konteks aman)
                teks_bersih = bersihkan_teks_minimal(teks_input)

                # 2. TF-IDF
                teks_vektor = vectorizer.transform([teks_bersih])

                # 3. Probabilitas
                probabilitas = model.predict_proba(teks_vektor)[0]

                prob_fakta = probabilitas[0]
                prob_hoax = probabilitas[1]

                # 🔥 4. THRESHOLD BARU (LEBIH KETAT)
                threshold = 0.85

                if prob_hoax > threshold:
                    label = "🚨 Berpotensi Hoaks"
                    warna = "error"
                    confidence = prob_hoax

                elif prob_hoax > 0.6:
                    label = "⚠️ Perlu Verifikasi"
                    warna = "warning"
                    confidence = prob_hoax

                else:
                    label = "✅ Kemungkinan Fakta"
                    warna = "success"
                    confidence = prob_fakta

                # Confidence level
                confidence_percent = confidence * 100

                if confidence_percent > 80:
                    tingkat = "Tinggi"
                elif confidence_percent > 60:
                    tingkat = "Sedang"
                else:
                    tingkat = "Rendah"

                # --- OUTPUT ---
                st.divider()
                st.subheader("Hasil Analisis:")

                if warna == "error":
                    st.error(label)
                elif warna == "warning":
                    st.warning(label)
                else:
                    st.success(label)

                st.progress(
                    confidence,
                    text=f"Tingkat Keyakinan: {confidence_percent:.2f}% ({tingkat})"
                )

                st.caption("⚠️ Model AI tidak selalu benar, gunakan sebagai alat bantu analisis.")

                # --- DETAIL ---
                with st.expander("Lihat Detail Proses"):

                    st.markdown("**1. Teks Asli:**")
                    st.write(f"*{teks_input}*")

                    st.markdown("**2. Teks Setelah Preprocessing:**")
                    st.info(teks_bersih)

                    st.markdown("**3. Probabilitas Model:**")

                    df_prob = pd.DataFrame({
                        'Kelas': ['Fakta', 'Hoaks'],
                        'Probabilitas': [
                            f"{prob_fakta*100:.2f}%",
                            f"{prob_hoax*100:.2f}%"
                        ]
                    })

                    st.table(df_prob)