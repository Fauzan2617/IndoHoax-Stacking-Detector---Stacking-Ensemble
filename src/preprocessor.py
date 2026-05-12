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