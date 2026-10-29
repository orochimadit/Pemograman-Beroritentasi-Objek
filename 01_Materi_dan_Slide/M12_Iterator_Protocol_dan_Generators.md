# 📘 Modul 12: Iterator Protocol & Generator Objects

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami perbedaan antara objek **Iterable** dan objek **Iterator**.
2. Mengimplementasikan protokol iterator dengan dunder method `__iter__` dan `__next__`.
3. Memahami cara kerja keyword `yield` dan fungsi generator untuk pemrosesan data besar (*streaming*).
4. Mencegah kehabisan memori (*Out-Of-Memory / OOM*) melalui konsep evaluasi lambat (*lazy evaluation*).

---

## 1. Bagaimana Python Melakukan Iterasi?

Ketika Anda menulis loop `for item in koleksi:`, di balik layar Python menjalankan protokol berikut:
1. Memanggil `iter(koleksi)` yang mengeksekusi `koleksi.__iter__()` untuk mendapatkan objek iterator.
2. Memanggil `next(iterator)` atau `iterator.__next__()` berulang kali untuk mengambil nilai berikutnya.
3. Berhenti saat iterator memicu exception bawaan `StopIteration`.

```
[ Iterable Object ]  ── __iter__() ──>  [ Iterator Object ]
                                               │
                                         __next__() -> Nilai 1
                                         __next__() -> Nilai 2
                                         __next__() -> StopIteration (Selesai)
```

---

## 2. Studi Kasus Demo: Streaming Pembaca File Log

Membaca file log 5 GB sekaligus ke dalam `list` menggunakan `f.readlines()` akan langsung membuat memori RAM penuh dan program macet (*crash*). Kita buat class Iterator yang membaca baris demi baris secara cerdas (*lazy*).

```python
from typing import Iterator

class LogFileIterator:
    """Class Iterator murni yang membaca file secara bertahap"""
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.file = None

    def __iter__(self) -> "LogFileIterator":
        # Buka file dan kembalikan diri sendiri sebagai iterator
        self.file = open(self.file_path, "r", encoding="utf-8")
        return self

    def __next__(self) -> str:
        line = self.file.readline()
        if not line:
            # Selesai membaca file, tutup resource dan hentikan iterasi
            self.file.close()
            raise StopIteration
        return line.strip()


class ErrorLogScanner:
    """Class generator yang menyaring hanya baris dengan status ERROR"""
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def scan_errors(self) -> Iterator[str]:
        """Generator function menggunakan keyword yield"""
        with open(self.file_path, "r", encoding="utf-8") as f:
            for baris in f:
                if "[ERROR]" in baris or "[FATAL]" in baris:
                    yield baris.strip()  # Mengalirkan data satu per satu tanpa makan memori!
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Paginasi Katalog Produk (E-Commerce Paginator)
1. **Rancang Class `ProductPaginator`**:
   - Atribut: `total_items: int = 100_000`, `page_size: int = 20`.
   - Implementasikan protokol `__iter__` dan `__next__`:
     - Setiap pemanggilan iterasi mengembalikan 1 halaman (berisi list dummy 20 produk).
     - Berhenti secara aman dengan `StopIteration` saat seluruh halaman selesai.
2. **Uji Efisiensi Memori Menggunakan `sys.getsizeof`**:
   - Bandingkan konsumsi memori antara:
     - Cara 1: Meng-generate list 100.000 objek sekaligus di memori.
     - Cara 2: Menggunakan class `ProductPaginator` berbasis generator/iterator.
3. **Instruksi Vibe Coding**:
   - Arahkan AI membuat simulasi tersebut.
   - Ambil tangkapan layar atau salin output perbedaan ukuran bytes memori di terminal, lalu lampirkan di `PROMPT_LOG.md`.
