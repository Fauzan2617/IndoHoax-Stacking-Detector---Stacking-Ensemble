import re  # Library untuk manipulasi teks (regex)

# Import Sastrawi untuk NLP Bahasa Indonesia
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


# ============================================================
# Inisialisasi Sastrawi (sekali saja)
# ============================================================

stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()


# ============================================================
# 🔥 Encoding Label + Cleaning Label
# ============================================================

def clean_label(label):
    """
    Membersihkan label dari noise seperti:
    - spasi
    - huruf besar/kecil
    - karakter aneh
    
    Contoh:
    ' HOAX ' → 'hoax'
    """
    return str(label).strip().lower()


def encode_label(label):
    """
    Mengubah label teks menjadi numerik.

    Mapping:
    - valid → 0
    - hoax  → 1

    Label lain akan dikembalikan sebagai None
    agar bisa difilter.
    """

    mapping = {
        'valid': 0,
        'hoax': 1
    }

    label = clean_label(label)

    return mapping.get(label, None)  
    # 🔥 kalau tidak ada di mapping → None (bukan error)


def encode_label_series(series):
    """
    Encode label + return full series (tidak dipotong)
    """

    encoded = series.apply(encode_label)

    valid_mask = encoded.notnull()

    return encoded, valid_mask


# ============================================================
# Fungsi preprocessing teks (FULL)
# ============================================================

def bersihkan_teks_total(teks):
    """
    Preprocessing lengkap:
    - lowercase
    - hapus URL
    - hapus mention & hashtag
    - hapus non huruf
    - hapus stopword
    - stemming
    """

    teks = str(teks).lower()

    teks = re.sub(r'http\S+|www\S+|https\S+', '', teks, flags=re.MULTILINE)
    teks = re.sub(r'\@\w+|\#', '', teks)
    teks = re.sub(r'[^a-zA-Z\s]', '', teks)

    teks = stopword.remove(teks)
    teks = stemmer.stem(teks)

    return teks


# ============================================================
# Fungsi preprocessing teks (MINIMAL)
# ============================================================

def bersihkan_teks_minimal(teks):
    """
    Preprocessing minimal (untuk simulasi noisy data)
    """

    teks = str(teks).lower()

    teks = re.sub(r'http\S+|www\S+|https\S+', '', teks, flags=re.MULTILINE)

    return teks