# 🎓 Panduan Tugas Besar & Evaluasi Akhir Semester (UAS)
## MATA KULIAH: PEMROGRAMAN BERORIENTASI OBJEK (PBO)

---

### 🎯 Deskripsi Proyek Akhir
Tugas Besar UAS bertujuan untuk menguji kemampuan menyeluruh mahasiswa dalam merancang, membangun, menguji, dan memelihara aplikasi perangkat lunak berbasis **Pemrograman Berorientasi Objek (PBO)** skala menengah dengan menerapkan metode **Vibe Coding**.

Mahasiswa bertindak sebagai **Lead Software Architect** dan **Quality Assurance Engineer** yang bertanggung jawab atas rancang bangun sistem, kepatuhan prinsip OOP, dan integritas kode program.

---

### 📌 Persyaratan Teknis Proyek (Spesifikasi Wajib)

Setiap proyek wajib memenuhi kriteria arsitektur berikut:

1. **Penerapan 4 Pilar PBO**:
   - **Enkapsulasi**: Menggunakan decorator `@property` untuk validasi data sensitif/kritis.
   - **Pewarisan & Komposisi**: Menggunakan *composition over inheritance* di tempat yang tepat, serta pewarisan yang mematuhi *Liskov Substitution Principle*.
   - **Polimorfisme**: Menggunakan method overriding yang konsisten antar turunan class.
   - **Abstraksi**: Menggunakan modul `abc` (`ABC` & `@abstractmethod`) untuk mendefinisikan antarmuka kontrak sistem.

2. **Penggunaan Pythonic OOP Modern**:
   - Memanfaatkan `@dataclass` untuk entitas transfer data / model.
   - Mengimplementasikan minimal 2 *Magic / Dunder Methods* (misal: `__str__`, `__repr__`, `__len__`, `__eq__`, atau `__add__`).
   - Hirarki *Custom Exception* berbasis domain aplikasi (dilarang menggunakan generic `raise Exception`).

3. **Penerapan Pola Desain (Minimal 2 Design Patterns)**:
   - Pilih minimal **dua pola desain** yang relevan:
     - *Creational*: Factory Method atau Singleton.
     - *Structural*: Facade, Adapter, atau Decorator.
     - *Behavioral*: Strategy atau Observer.

4. **Jaminan Kualitas via Automated Testing (`pytest`)**:
   - Menyertakan file `test_core.py` dengan minimal **10 test cases** yang menguji skenario positif (*happy path*) maupun skenario penolakan (*exception & edge cases*).

---

### 📂 Struktur Repositori Pengumpulan

```text
Kelompok_XX_TugasBesar_PBO/
├── docs/
│   ├── ARSITEKTUR_DAN_UML.md    # Diagram Class (Mermaid), alasan pemilihan pattern
│   └── PROMPT_LOG.md            # Dokumentasi iterasi Vibe Coding & Code Review
├── src/
│   ├── __init__.py
│   ├── models/                  # Entitas data & dataclass
│   ├── services/                # Logika bisnis & integrasi pola desain
│   ├── exceptions/              # Custom exception domain
│   └── main.py                  # Entry point aplikasi
├── tests/
│   ├── __init__.py
│   └── test_core.py             # Test suite pytest
├── README.md                    # Panduan instalasi & cara menjalankan aplikasi
└── requirements.txt             # Dependensi (pytest, dll)
```

---

### 📊 Rubrik Penilaian UAS (Skala 100)

| Kriteria | Bobot | Indikator Penilaian |
| :--- | :---: | :--- |
| **Arsitektur & Desain PBO** | 25% | Penerapan 4 pilar PBO yang tepat, pemisahan tanggung jawab (SRP), dan tidak ada *code smell* kaku. |
| **Penerapan Design Patterns** | 20% | Pemilihan 2 design patterns tepat guna dan terintegrasi secara natural dalam studi kasus. |
| **Kualitas Pengujian (`pytest`)** | 20% | Kelengkapan minimal 10 test cases, mencakup pengujian exception dan seluruh test berstatus *passed*. |
| **Metode Vibe Coding & Review** | 20% | Kualitas dokumen `PROMPT_LOG.md` yang membuktikan peran aktif mahasiswa mengkritisi dan mengarahkan AI. |
| **Presentasi & Demo Program** | 15% | Penguasaan materi saat sesi tanya jawab, penjelasan alur objek, dan demo aplikasi berjalan tanpa *error*. |
