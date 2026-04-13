import re  # Library untuk manipulasi teks menggunakan Regular Expression (regex)

# Import library Sastrawi untuk NLP Bahasa Indonesia
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory  # Untuk stemming (mengubah kata ke bentuk dasar)
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory  # Untuk menghapus stopword

# ============================================================
# Inisialisasi Sastrawi (dilakukan sekali saja, bukan di dalam fungsi)
# Tujuannya agar lebih efisien dan tidak dibuat ulang setiap pemanggilan fungsi
# ============================================================

stemmer = StemmerFactory().create_stemmer()  
# Membuat objek stemmer → contoh: "berlari" → "lari"

stopword = StopWordRemoverFactory().create_stop_word_remover()  
# Membuat objek stopword remover → menghapus kata umum seperti "dan", "yang", "di", dll


# ============================================================
# Fungsi preprocessing lengkap (untuk training model utama)
# ============================================================

def bersihkan_teks_total(teks):
    """
    Fungsi untuk membersihkan teks secara menyeluruh (full preprocessing).
    
    Tahapan:
    1. Lowercase
    2. Hapus URL
    3. Hapus mention & hashtag
    4. Hapus karakter non-alfabet
    5. Hapus stopword
    6. Stemming
    
    Cocok digunakan untuk training model utama agar performa maksimal.
    """

    teks = str(teks).lower()  
    # Mengubah teks menjadi string dan huruf kecil semua (normalisasi)

    teks = re.sub(r'http\S+|www\S+|https\S+', '', teks, flags=re.MULTILINE)  
    # Menghapus URL (http, https, www)
    # \S+ → semua karakter non-spasi setelah http/www

    teks = re.sub(r'\@\w+|\#', '', teks)  
    # Menghapus mention (@username) dan simbol hashtag (#)

    teks = re.sub(r'[^a-zA-Z\s]', '', teks)  
    # Menghapus semua karakter selain huruf (a-z, A-Z) dan spasi
    # Contoh: angka, simbol, tanda baca akan hilang

    teks = stopword.remove(teks)  
    # Menghapus stopword (kata umum yang tidak penting)
    # Contoh: "dan", "yang", "di", dll

    teks = stemmer.stem(teks)  
    # Mengubah kata ke bentuk dasar (stemming)
    # Contoh: "berlari", "lari-lari" → "lari"

    return teks  
    # Mengembalikan teks yang sudah dibersihkan total


# ============================================================
# Fungsi preprocessing minimal (untuk simulasi data noisy)
# ============================================================

def bersihkan_teks_minimal(teks):
    """
    Fungsi preprocessing sederhana (minimal cleaning).
    
    Tahapan:
    1. Lowercase
    2. Hapus URL saja
    
    Digunakan untuk:
    - Simulasi data dunia nyata (noisy data)
    - Uji robustness model
    """

    teks = str(teks).lower()  
    # Normalisasi teks ke huruf kecil

    teks = re.sub(r'http\S+|www\S+|https\S+', '', teks, flags=re.MULTILINE)  
    # Hanya menghapus URL, tanpa preprocessing lain

    return teks  
    # Mengembalikan teks yang masih "kotor" (realistic scenario)