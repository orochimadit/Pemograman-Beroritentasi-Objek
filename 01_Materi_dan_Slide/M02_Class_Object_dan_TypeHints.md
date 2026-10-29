# 📘 Modul 02: Objek, Class, State & Behavior, Type Hints

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Mendefinisikan class dan menginstansiasi objek di Python.
2. Memahami peran parameter `self` dan method inisialisasi `__init__`.
3. Menerapkan *Type Annotations / Type Hints* (PEP 484) secara konsisten pada atribut dan fungsi.
4. Membedakan *Class Attribute* (milik bersama) vs *Instance Attribute* (milik objek spesifik).

---

## 1. Anatomi Class dalam Python Modern

```python
class NamaClass:
    # Class Attribute (Berlaku global untuk semua objek dari class ini)
    jumlah_dibuat: int = 0

    def __init__(self, parameter_1: str, parameter_2: int) -> None:
        # Instance Attributes (Spesifik hanya untuk instance ini)
        self.parameter_1: str = parameter_1
        self.parameter_2: int = parameter_2
        NamaClass.jumlah_dibuat += 1

    def method_aksi(self, tambahan: int) -> str:
        # Instance Method (Perilaku objek)
        self.parameter_2 += tambahan
        return f"Nilai sekarang: {self.parameter_2}"
```

### 1.1 Mengapa Parameter `self` Wajib?
Di Python, `self` merujuk secara eksplisit pada *instance* objek yang sedang aktif memanggil method tersebut. Saat Anda menulis `objek.method_aksi(5)`, di balik layar Python mengeksekusinya sebagai:
`NamaClass.method_aksi(objek, 5)`.

### 1.2 Type Hints (Anotasi Tipe Data)
Type hints tidak mengubah cara Python mengeksekusi kode saat runtime, tetapi memberikan keuntungan besar:
- Dokumentasi otomatis langsung di IDE (*IntelliSense / autocomplete*).
- Menghindari bug fatal sebelum program dijalankan (*static type checking* via `mypy`).
- Memberikan instruksi yang jelas bagi AI Assistant saat melakukan *code generation*.

---

## 2. Studi Kasus Demo: Manajemen Buku Perpustakaan

```python
from typing import Optional

class Buku:
    # Class Attribute untuk melacak total inventaris
    total_koleksi_buku: int = 0

    def __init__(
        self,
        isbn: str,
        judul: str,
        penulis: str,
        stok_tersedia: int = 1
    ) -> None:
        self.isbn: str = isbn
        self.judul: str = judul
        self.penulis: str = penulis
        self.stok_tersedia: int = stok_tersedia
        self.sedang_dipinjam: bool = False
        Buku.total_koleksi_buku += stok_tersedia

    def pinjam(self) -> bool:
        if self.stok_tersedia > 0:
            self.stok_tersedia -= 1
            self.sedang_dipinjam = True
            print(f"Buku '{self.judul}' berhasil dipinjam. Sisa stok: {self.stok_tersedia}")
            return True
        print(f"Maaf, stok buku '{self.judul}' sedang kosong!")
        return False

    def kembalikan(self) -> None:
        self.stok_tersedia += 1
        self.sedang_dipinjam = False
        print(f"Buku '{self.judul}' telah dikembalikan. Stok sekarang: {self.stok_tersedia}")


class AnggotaPerpustakaan:
    def __init__(self, id_anggota: str, nama: str) -> None:
        self.id_anggota: str = id_anggota
        self.nama: str = nama
        self.daftar_pinjaman: list[Buku] = []

    def lakukan_peminjaman(self, buku: Buku) -> None:
        if buku.pinjam():
            self.daftar_pinjaman.append(buku)
            print(f"Buku berhasil ditambahkan ke riwayat {self.nama}.")


# Uji Coba Program
if __name__ == "__main__":
    b1 = Buku("978-01", "Python Object-Oriented Programming", "Dusty Phillips", stok_tersedia=2)
    b2 = Buku("978-02", "Clean Architecture", "Robert C. Martin", stok_tersedia=1)

    mhs1 = AnggotaPerpustakaan("A001", "Badra")
    mhs1.lakukan_peminjaman(b1)
    mhs1.lakukan_peminjaman(b2)
    
    # Mencoba pinjam buku yang stoknya sudah habis
    mhs2 = AnggotaPerpustakaan("A002", "Doni")
    mhs2.lakukan_peminjaman(b2)
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Rental Kendaraan Kampus
1. **Rancang Entitas**:
   - Class `Kendaraan`:
     - Atribut: `plat_nomor: str`, `merk: str`, `harga_per_hari: float`, `status_tersedia: bool = True`.
     - Method: `hitung_biaya_sewa(hari: int) -> float`, `ubah_status(tersedia: bool) -> None`.
   - Class `Pelanggan`:
     - Atribut: `nim: str`, `nama: str`, `telepon: str`, `sewaan_aktif: list[Kendaraan]`.
     - Method: `tambah_sewaan(kendaraan: Kendaraan, hari: int) -> float`.
2. **Instruksi Vibe Coding**:
   - Buka AI Assistant dan ketik prompt spesifikasi di atas.
   - **Tinjau Kode AI**: Pastikan setiap parameter dan return type menggunakan Type Hints (misal: `-> float`, `list[Kendaraan]`).
   - Minta AI menambahkan method `tampilkan_ringkasan()` yang mencetak nama penyewa beserta total biaya sewanya.
   - Dokumentasikan log prompt di `PROMPT_LOG.md`.
