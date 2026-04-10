import pickle
import os

def simpan_objek(obj, filepath):
    # Membuat folder jika belum ada
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f)

def load_objek(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)