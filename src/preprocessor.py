import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Inisialisasi Sastrawi (dilakukan di luar fungsi agar tidak diload berulang kali)
stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()

def bersihkan_teks_total(teks):
    teks = str(teks).lower()
    teks = re.sub(r'http\S+|www\S+|https\S+', '', teks, flags=re.MULTILINE) # Hapus URL
    teks = re.sub(r'\@\w+|\#', '', teks) # Hapus mention & hashtag
    teks = re.sub(r'[^a-zA-Z\s]', '', teks) # Hapus karakter non-alfabet
    teks = stopword.remove(teks) # Hapus stopword
    teks = stemmer.stem(teks) # Stemming
    return teks

def bersihkan_teks_minimal(teks):
    # Untuk simulasi data noisy (hanya hapus URL)
    teks = str(teks).lower()
    teks = re.sub(r'http\S+|www\S+|https\S+', '', teks, flags=re.MULTILINE)
    return teks