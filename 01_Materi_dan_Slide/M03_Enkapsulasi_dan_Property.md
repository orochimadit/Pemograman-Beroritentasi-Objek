# 📘 Modul 03: Enkapsulasi, Proteksi State, & Decorator `@property`

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami konsep pilar pertama PBO: **Enkapsulasi** (Information Hiding).
2. Memahami filosofi enkapsulasi di Python: konvensi `_protected` dan *name mangling* `__private`.
3. Menggunakan decorator `@property` dan `@<nama>.setter` untuk membuat antarmuka data yang aman dan *Pythonic*.
4. Mencegah pelanggaran integritas state objek (*state invariant*).

---

## 1. Mengapa Enkapsulasi Sangat Krusial?

Enkapsulasi bertujuan melindungi data internal objek agar tidak dapat dimodifikasi sembarangan oleh kode eksternal yang dapat merusak konsistensi data (*state corruption*).

```
[ KODE LUAR ]
      |
      |   ❌ dilarang ubah langsung: dompet._saldo = -999999
      v
+-----------------------------------------------------------+
|                        CLASS EWALLET                      |
|                                                           |
|   [ VALIDATOR SETTER ]                                    |
|   Apakah saldo baru >= 0?                                 |
|      /              \                                     |
|   (YA)             (TIDAK)                                |
|    v                 v                                    |
|  Simpan          Tolak & Lemparkan ValueError             |
|                                                           |
|  [ INTERNAL STATE ]: _saldo                               |
+-----------------------------------------------------------+
```

---

## 2. Enkapsulasi Bergaya Java vs Idiom Pythonic

### 2.1 Cara Lama (Java Style di Python - Kurang Direkomendasikan)
```python
# ⚠️ Sintaks kaku yang tidak disukai komunitas Python
class DompetLama:
    def __init__(self, saldo: float) -> None:
        self.__saldo = saldo

    def get_saldo(self) -> float:
        return self.__saldo

    def set_saldo(self, nilai: float) -> None:
        if nilai < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        self.__saldo = nilai
```

### 2.2 Cara Modern (Pythonic dengan `@property`)
Dengan `@property`, pengguna class dapat mengakses atribut secara natural (`dompet.saldo`), namun di balik layar dieksekusi melalui fungsi validasi.

```python
class EWallet:
    def __init__(self, pemilik: str, saldo_awal: float = 0.0) -> None:
        self.pemilik: str = pemilik
        self._saldo: float = 0.0  # Atribut internal yang dilindungi
        self.saldo = saldo_awal   # Melewati validasi setter!

    @property
    def saldo(self) -> float:
        """Getter untuk membaca saldo"""
        return self._saldo

    @saldo.setter
    def saldo(self, nilai: float) -> None:
        """Setter dengan filter validasi ketat"""
        if nilai < 0:
            raise ValueError(f"Validasi Gagal: Saldo tidak boleh negatif! (Input: {nilai})")
        self._saldo = nilai

    def tarik_tunai(self, jumlah: float) -> None:
        if jumlah <= 0:
            raise ValueError("Jumlah penarikan harus lebih dari 0!")
        if jumlah > self._saldo:
            raise ValueError(f"Saldo tidak cukup! Saldo Anda: {self._saldo}, diminta: {jumlah}")
        self._saldo -= jumlah
        print(f"Penarikan Rp {jumlah:,.2f} sukses. Sisa saldo: Rp {self._saldo:,.2f}")
```

---

## 3. Atribut Terhitung (*Computed Read-Only Properties*)
Salah satu kekuatan terbesar `@property` adalah membuat properti dinamis tanpa setter, sehingga nilainya **hanya bisa dibaca (*read-only*)** dan selalu akurat.

```python
class Mahasiswa:
    def __init__(self, nama: str, total_poin_sks: float, total_sks: int) -> None:
        self.nama = nama
        self.total_poin_sks = total_poin_sks
        self.total_sks = total_sks

    @property
    def ipk(self) -> float:
        """Nilai IPK dihitung secara real-time. Tidak bisa diedit manual dari luar."""
        if self.total_sks == 0:
            return 0.0
        return round(self.total_poin_sks / self.total_sks, 2)

m = Mahasiswa("Ahmad", total_poin_sks=72.0, total_sks=20)
print(m.ipk)  # Output: 3.6
# m.ipk = 4.0  -> ❌ Akan menghasilkan AttributeError: property 'ipk' has no setter
```

---

## 4. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Nilai Akademik & Transkrip Mahasiswa
1. **Buat Class `NilaiMataKuliah`**:
   - Atribut internal `_nilai_angka` (float).
   - `@property def nilai_angka` dan setter-nya:
     - Jika input < 0 atau > 100, lempar `ValueError("Nilai harus berada dalam rentang 0 - 100")`.
   - `@property def nilai_huruf` (Read-only):
     - $\ge 85$: 'A', $\ge 70$: 'B', $\ge 55$: 'C', $\ge 40$: 'D', $< 40$: 'E'.
   - `@property def status_kelulusan` (Read-only):
     - Mengembalikan `"LULUS"` jika nilai huruf A, B, atau C. Mengembalikan `"TIDAK LULUS"` jika D atau E.
2. **Instruksi Vibe Coding**:
   - Buka AI Assistant dan perintahkan membuat class tersebut.
   - **Uji Kualitas AI**: Cobalah assign `nilai_huruf = 'A'`. Pastikan program memunculkan error karena properti tersebut harus *read-only*.
   - Jika AI ternyata membuat setter untuk `nilai_huruf`, instruksikan AI untuk menghapusnya!
   - Simpan kode di `03_Tugas_dan_Latihan/tugas_m03_enkapsulasi.py` dan catat prompt-nya di `PROMPT_LOG.md`.
