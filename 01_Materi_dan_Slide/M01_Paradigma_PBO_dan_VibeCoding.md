# 📘 Modul 01: Paradigma PBO & Pengantar Metode Vibe Coding

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Menjelaskan perbedaan mendasar antara paradigma pemrograman prosedural dan berorientasi objek (PBO).
2. Memahami prinsip dasar *Object-Oriented Design* (OOD): Entitas, State (Atribut), dan Behavior (Method).
3. Memahami peran baru programmer dalam era *Vibe Coding*: beralih dari sekadar pengetik kode (*code monkey*) menjadi *System Architect* dan *Code Reviewer*.
4. Mengonfigurasi lingkungan kerja (*development environment*) Python 3.10+, VS Code, dan AI Coding Assistant.

---

## 1. Pemrograman Prosedural vs Pemrograman Berorientasi Objek

### 1.1 Keterbatasan Pendekatan Prosedural
Pada paradigma prosedural, program dibagi menjadi fungsi-fungsi yang mengolah data global atau struktur data terpisah (seperti dictionary, tuple, atau list).

```python
# ❌ Pendekatan Prosedural yang Rawan Bug
pasien_1 = {"nama": "Budi", "umur": 28, "keluhan": "Demam", "status": "Menunggu"}
pasien_2 = {"nama": "Siti", "usia": 22, "gejala": "Pusing"}  # Inkonsistensi kunci kamus!

def panggil_pasien(pasien):
    # Tidak ada jaminan pasien memiliki kunci 'status'
    pasien["status"] = "Sedang Diperiksa"
    print(f"Memanggil pasien: {pasien['nama']}")

panggil_pasien(pasien_2)  # KeyError atau modifikasi data tak terkontrol!
```

**Kelemahan Utama Prosedural:**
- Data dan fungsi terpisah, sehingga fungsi luar mana pun bisa memanipulasi data tanpa kendali (*uncontrolled side-effects*).
- Inkonsistensi struktur data (*dictionary keys* mudah salah ketik/berubah).
- Sulit dimaintain dan diperluas saat sistem berkembang menjadi ribuan baris.

---

### 1.2 Pendekatan Berorientasi Objek (OOP / PBO)
PBO membungkus **data (state)** dan **fungsi yang mengolahnya (behavior)** ke dalam satu kesatuan utuh yang disebut **Objek**.

```
+----------------------------------------------------+
|                       OBJEK                        |
|                                                    |
|  [ STATE / DATA ]                                  |
|  - nama: "Budi"                                    |
|  - nomor_antrean: 101                              |
|  - status: "Menunggu"                              |
|                                                    |
|  [ BEHAVIOR / METHOD ]                             |
|  + panggil()                                       |
|  + selesai_periksa()                               |
|  + batalkan()                                      |
+----------------------------------------------------+
```

---

## 2. Apa itu Vibe Coding dalam Konteks PBO?

### 2.1 Paradigma "Vibe Coding"
Dipopulerkan oleh Andrej Karpathy (2025), *Vibe Coding* adalah metode pengembangan aplikasi di mana programmer berinteraksi dengan AI Coding Assistant secara iteratif dalam bahasa alami tingkat tinggi.

```
+-------------------+      Prompt Arsitektur       +---------------------+
|                   | ---------------------------> |                     |
|     MAHASISWA     |                              |     AI ASSISTANT    |
| (System Architect | <--------------------------- | (Draft Code & Test) |
|  & Code Reviewer) |       Inspeksi & Review      |                     |
+-------------------+                              +---------------------+
          |
          v Loop Verifikasi (Run, Pytest, Refactor)
```

### 2.2 Mengapa Mahasiswa PBO Harus Memahami Arsitektur?
Jika mahasiswa tidak paham PBO, prompt yang diberikan kepada AI akan menghasilkan kode yang buruk (*AI Spaghetti Slop*). Mahasiswa yang menguasai PBO mampu mengarahkan AI:
1. Menyusun struktur class yang modular.
2. Memisahkan *Single Responsibility*.
3. Mencegah *tight coupling*.

---

## 3. Studi Kasus Demo Kuliah: Sistem Antrean Pasien

Berikut implementasi PBO bersih di Python:

```python
"""
Sistem Antrean Klinik Sederhana berbasis PBO
"""
from datetime import datetime

class Pasien:
    def __init__(self, nomor_antrean: int, nama: str, keluhan: str) -> None:
        self.nomor_antrean = nomor_antrean
        self.nama = nama
        self.keluhan = keluhan
        self.waktu_daftar = datetime.now()
        self.status = "Menunggu"

    def panggil(self) -> None:
        self.status = "Sedang Diperiksa"
        print(f"[PANGGILAN] Nomor {self.nomor_antrean}: {self.nama} menuju ruang dokter.")

    def selesai(self) -> None:
        self.status = "Selesai"
        print(f"[SELESAI] Pasien {self.nama} telah menyelesaikan pemeriksaan.")


class AntreanKlinik:
    def __init__(self, nama_poli: str) -> None:
        self.nama_poli = nama_poli
        self.daftar_pasien: list[Pasien] = []

    def daftar_pasien_baru(self, nama: str, keluhan: str) -> Pasien:
        nomor_baru = len(self.daftar_pasien) + 1
        pasien_baru = Pasien(nomor_antrean=nomor_baru, nama=nama, keluhan=keluhan)
        self.daftar_pasien.append(pasien_baru)
        print(f"Pendaftaran berhasil: {nama} (No. Antrean: {nomor_baru}) di {self.nama_poli}")
        return pasien_baru


# Demo Eksekusi
if __name__ == "__main__":
    poli_umum = AntreanKlinik("Poli Umum")
    p1 = poli_umum.daftar_pasien_baru("Budi Santoso", "Demam tinggi")
    p2 = poli_umum.daftar_pasien_baru("Siti Rahma", "Pemeriksaan mata rutin")
    
    p1.panggil()
    p1.selesai()
```

---

## 4. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Perancangan Sistem Kafe Kampus
1. **Instruksi Analisis**: Jangan buka AI terlebih dahulu! Buat sketsa di kertas / Markdown daftar entitas objek untuk sistem pesanan kafe:
   - Entitas: `ItemMenu`, `Pesanan`, `MejaKafe`.
   - Sebutkan atribut dan perilakunya masing-masing.
2. **Instruksi Vibe Coding**:
   - Arahkan AI Assistant untuk membuat class sesuai sketsa Anda.
   - Periksa apakah AI membungkus data dengan class atau justru memakai dictionary sembarangan.
   - Buat file `PROMPT_LOG.md` yang mencatat minimal 2 kali revisi prompt terhadap kode AI.
