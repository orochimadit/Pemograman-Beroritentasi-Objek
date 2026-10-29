# 📘 Modul 10: Struktur Data Modern & Python Dataclasses

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami tujuan dan cara kerja decorator `@dataclass` (PEP 557).
2. Menghindari penulisan kode repetitif (*boilerplate code*) untuk `__init__`, `__repr__`, dan `__eq__`.
3. Menggunakan fitur lanjutan dataclass: `frozen=True` (objek yang tidak bisa diubah / *immutable*), `field(default_factory=...)`, dan method validasi `__post_init__`.
4. Memahami kapan harus menggunakan `@dataclass` vs class reguler.

---

## 1. Masalah *Boilerplate* pada Class Data Tradisional

Ketika kita hanya ingin membuat class untuk menyimpan data (seperti entitas database atau payload API), class reguler terasa sangat bertele-tele:

```python
# ❌ Cara Lama (Repetitif & Membosankan)
class PenggunaLama:
    def __init__(self, id_user: int, nama: str, email: str) -> None:
        self.id_user = id_user
        self.nama = nama
        self.email = email

    def __repr__(self) -> str:
        return f"PenggunaLama(id_user={self.id_user}, nama='{self.nama}', email='{self.email}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PenggunaLama):
            return False
        return (self.id_user, self.nama, self.email) == (other.id_user, other.nama, other.email)
```

---

## 2. Solusi Elegan: Python `@dataclass`

Dengan `@dataclass`, seluruh method di atas di-generate secara otomatis di balik layar!

```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)  # frozen=True membuat objek bersifat read-only (immutable)
class Alamat:
    jalan: str
    kota: str
    kode_pos: str


@dataclass
class PesananKonser:
    id_pesanan: str
    nama_pemesan: str
    harga_tiket: float
    jumlah_tiket: int
    # ⚠️ Default argument untuk mutable (list/dict) WAJIB menggunakan default_factory!
    daftar_kursi: list[str] = field(default_factory=list)
    waktu_pesan: datetime = field(default_factory=datetime.now)

    def __post_init__(self) -> None:
        """Dijalankan otomatis tepat setelah __init__ selesai dibuat"""
        if self.jumlah_tiket <= 0:
            raise ValueError("Jumlah tiket yang dipesan minimal 1!")
        if self.harga_tiket < 0:
            raise ValueError("Harga tiket tidak boleh bernilai negatif!")

    @property
    def total_tagihan(self) -> float:
        return self.harga_tiket * self.jumlah_tiket


# Uji Coba Dataclass
if __name__ == "__main__":
    pesanan = PesananKonser(
        id_pesanan="ORD-2026-001",
        nama_pemesan="Badra",
        harga_tiket=750_000.0,
        jumlah_tiket=2,
        daftar_kursi=["VIP-A1", "VIP-A2"]
    )

    # Otomatis memiliki representasi print yang rapi!
    print(pesanan)
    print(f"Total Bayar: Rp {pesanan.total_tagihan:,.2f}")

    alamat = Alamat("Jl. Ahmad Yani No. 10", "Pontianak", "78124")
    # alamat.kota = "Jakarta"  -> ❌ Menghasilkan FrozenInstanceError!
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Tiket Konser & Seat Map
1. **Buat `@dataclass(frozen=True)` untuk Objek `Seat`**:
   - Atribut: `baris: str`, `nomor: int`, `kategori: str` ("VIP", "Festival", "Tribun").
2. **Buat `@dataclass` untuk `TiketKonser`**:
   - Atribut: `kode_tiket: str`, `seat: Seat`, `harga_dasar: float`.
   - Gunakan `__post_init__` untuk validasi:
     - Jika `seat.kategori == "VIP"` dan `harga_dasar < 1_500_000`, lemparkan `ValueError("Harga tiket VIP minimal Rp 1.500.000!")`.
3. **Instruksi Vibe Coding**:
   - Instruksikan AI mengonversi class biasa menjadi `@dataclass`.
   - **Perangkap AI**: Perhatikan apakah AI menulis atribut `tags: list[str] = []` secara langsung. Ingatkan AI bahwa ini memicu *bug mutable default*, dan paksa AI untuk memakai `field(default_factory=list)`.
   - Simpan kode di `03_Tugas_dan_Latihan/tugas_m10_dataclass.py` dan dokumentasikan di `PROMPT_LOG.md`.
