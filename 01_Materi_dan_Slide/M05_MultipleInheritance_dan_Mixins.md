# 📘 Modul 05: Multiple Inheritance & Mixin Pattern

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami konsep pewarisan berganda (*Multiple Inheritance*) di Python.
2. Memahami permasalahan *Diamond Problem* dan cara penyelesaiannya dengan *Method Resolution Order* (MRO).
3. Merancang dan menerapkan **Mixin Pattern** untuk menyematkan fitur modular tanpa mengorbankan hierarki class.
4. Menganalisis urutan penelusuran method menggunakan atribut `Class.__mro__`.

---

## 1. Multiple Inheritance & The Diamond Problem

Di beberapa bahasa seperti Java atau C#, class hanya boleh memiliki satu induk (*single inheritance*). Namun, Python memperbolehkan satu class mewarisi lebih dari satu induk sekaligus.

```
            [ BaseClass A ]
               /        \
              /          \
      [ Class B ]      [ Class C ]
              \          /
               \        /
            [ Class D (B, C) ]  <-- The Diamond Problem
```

Jika Class B dan Class C sama-sama meng-override method `proses()`, method milik siapa yang akan dijalankan oleh Class D?
Python menyelesaikannya menggunakan algoritma **C3 Superclass Linearization**, yang dapat kita periksa melalui urutan **MRO (Method Resolution Order)**:
```python
print(D.__mro__)
# Output: (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

---

## 2. Pola Desain Mixin (*The Mixin Pattern*)

**Mixin** adalah class kecil yang berdiri sendiri, tidak dimaksudkan untuk diinstansiasi langsung, melainkan dirancang khusus untuk "dicampurkan" (*mixed-in*) ke dalam class lain guna menambah kemampuan tertentu.

### Ciri Khas Mixin:
- Nama class biasanya berakhiran `...Mixin`.
- Tidak memiliki state berat / constructor `__init__` kompleks.
- Bersifat dapat dipakai ulang (*reusable*) di banyak class yang tidak berhubungan hierarki.

---

## 3. Studi Kasus Demo: Mixin Ekspor JSON & Timestamp

```python
import json
from datetime import datetime

class TimestampMixin:
    """Mixin untuk otomatis mencatat waktu pembuatan objek"""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class JSONExportMixin:
    """Mixin untuk mengekspor atribut publik objek menjadi format JSON string"""
    def to_json(self) -> str:
        # Ambil semua atribut instance yang tidak diawali underscore
        data = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return json.dumps(data, indent=2, ensure_ascii=False)


# Base Class Bisnis
class Produk:
    def __init__(self, sku: str, nama: str, harga: float) -> None:
        self.sku = sku
        self.nama = nama
        self.harga = harga


# Class Akhir: Mewarisi Produk + Disematkan 2 Mixin Sekaligus
class ProdukECommerce(TimestampMixin, JSONExportMixin, Produk):
    def __init__(self, sku: str, nama: str, harga: float, kategori: str) -> None:
        self.kategori = kategori
        # Panggil chain inisialisasi MRO
        super().__init__(sku=sku, nama=nama, harga=harga)


# Uji Coba Program
if __name__ == "__main__":
    laptop = ProdukECommerce(
        sku="LP-ROG-001",
        nama="Asus ROG Strix G16",
        harga=24_500_000,
        kategori="Laptop Gaming"
    )

    print("=== DATA PRODUK DALAM FORMAT JSON ===")
    print(laptop.to_json())
    print("\nUrutan MRO Class:")
    for cls in ProdukECommerce.__mro__:
        print(f" -> {cls.__name__}")
```

---

## 4. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Entitas Berfitur Tracking
1. **Buat Dua Mixin Mandiri**:
   - `AuditLogMixin`:
     - Method: `log_aktivitas(aktivitas: str) -> None` yang mencetak: `"[AUDIT] <nama_class> (<id_entitas>): <aktivitas> pada <timestamp>"`.
   - `SoftDeleteMixin`:
     - Atribut: `is_deleted: bool = False`, `deleted_at: str | None = None`.
     - Method: `soft_delete() -> None` yang mengubah `is_deleted = True` dan mengisi `deleted_at`.
2. **Terapkan pada Class `Pengguna` dan `KuponDiskon`**:
   - `Pengguna`: Atribut `id_user`, `email`.
   - `KuponDiskon`: Atribut `kode_kupon`, `persen_diskon`.
3. **Instruksi Vibe Coding**:
   - Minta AI menerapkan Mixin di atas.
   - Periksa urutan inheritance: Pastikan Mixin diletakkan di sisi kiri sebelum base class (`class Pengguna(AuditLogMixin, SoftDeleteMixin, BaseEntity)`).
   - Tampilkan output `Pengguna.__mro__` di terminal dan lampirkan di `PROMPT_LOG.md`.
