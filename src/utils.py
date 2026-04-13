import pickle  # Library untuk menyimpan dan memuat objek Python (serialization)
import os      # Library untuk berinteraksi dengan sistem operasi (file & folder)


# Fungsi dibawah untuk menyimpan object dalam bentuk apapun 
def simpan_objek(obj, filepath):
    """
    Fungsi untuk menyimpan objek Python ke dalam file menggunakan pickle.
    
    Parameter:
    - obj      : objek Python yang ingin disimpan (model, data, dll)
    - filepath : lokasi file tujuan (contoh: 'data/models/model.pkl')
    """

    # Membuat folder tujuan jika belum ada
    # os.path.dirname(filepath) → mengambil path folder dari filepath
    # exist_ok=True → tidak error jika folder sudah ada
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Membuka file dalam mode 'wb' (write binary)
    # 'wb' digunakan karena pickle menyimpan data dalam bentuk biner
    with open(filepath, 'wb') as f:
        
        # Menyimpan (serialize) objek ke dalam file
        pickle.dump(obj, f)



# Fungsi dibawah untuk mengload kembali data yang disimpan
def load_objek(filepath):
    """
    Fungsi untuk memuat kembali objek Python dari file pickle.
    
    Parameter:
    - filepath : lokasi file yang akan dibaca
    
    Return:
    - objek Python yang sudah disimpan sebelumnya
    """

    # Membuka file dalam mode 'rb' (read binary)
    # 'rb' digunakan untuk membaca file biner hasil pickle
    with open(filepath, 'rb') as f:
        
        # Membaca dan mengembalikan (deserialize) objek dari file
        return pickle.load(f)