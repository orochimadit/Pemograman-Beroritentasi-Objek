# 📘 RENCANA PEMBELAJARAN SEMESTER (RPS)
## MATA KULIAH: PEMROGRAMAN BERORIENTASI OBJEK (PBO)
### Pendekatan: Modern Python & Vibe Coding (AI-Assisted Software Architecture)

---

### 🎯 Informasi Mata Kuliah
- **Mata Kuliah**: Pemrograman Berorientasi Objek (Object-Oriented Programming)
- **Dosen Pengampu / Pemateri**: Aditya Pratama
- **Bobot**: 3 SKS (2 Teori, 1 Praktikum)
- **Bahasa Utama**: Python 3.10+ (Type Hints PEP 484)
- **Buku Referensi Utama**: *Python Object-Oriented Programming (4th Edition)* - Dusty Phillips & Steven F. Lott (Packt Publishing)
- **Metode Pembelajaran**: *Vibe Coding Framework* (Peran mahasiswa sebagai System Architect, Code Reviewer, dan Quality Verifier dengan bantuan AI Assistant)

---

### 🏆 Capaian Pembelajaran Mata Kuliah (CPMK)
1. **CPMK-1 (Conceptual Foundation)**: Mahasiswa mampu menjelaskan perbedaan paradigma prosedural dan PBO serta prinsip dasar *Object-Oriented Design* (OOD).
2. **CPMK-2 (Four Pillars of OOP)**: Mahasiswa mampu mengimplementasikan dan mengkritisi 4 pilar PBO (Enkapsulasi, Pewarisan, Polimorfisme, dan Abstraksi) secara *Pythonic*.
3. **CPMK-3 (Design Patterns & Pythonic Idioms)**: Mahasiswa mampu menerapkan pola desain (GoF patterns), Abstract Base Classes, dunder methods, dan dataclasses untuk memecahkan masalah rekayasa perangkat lunak.
4. **CPMK-4 (Vibe Coding & Quality Assurance)**: Mahasiswa mampu mengarahkan AI Coding Assistant secara terstruktur (architectural prompting), mengidentifikasi *code smells*, serta melakukan verifikasi logika objek dengan *automated unit testing* (`pytest`).

---

### 🗓️ Rencana 16 Pertemuan Perkuliahan

```
SEMESTER BREAKDOWN:
├── BLOK 1: FONDASI & PEMODELAN OBJEK (Minggu 1 - 3)
├── BLOK 2: EMPAT PILAR PBO & ERROR HANDLING (Minggu 4 - 7)
├── EVALUASI TENGAH SEMESTER (Minggu 8: UTS)
├── BLOK 3: PYTHONIC OOP & ADVANCED STRUCTURES (Minggu 9 - 12)
├── BLOK 4: DESIGN PATTERNS, TESTING & PROYEK (Minggu 13 - 15)
└── EVALUASI AKHIR SEMESTER (Minggu 16: UAS / Project Showcase)
```

---

#### 📌 BLOK 1: FONDASI & PEMODELAN OBJEK

##### Minggu 01: Paradigma PBO & Pengantar Metode Vibe Coding
- **Materi Teori**: 
  - Keterbatasan paradigma prosedural pada sistem berskala besar.
  - Prinsip *Object-Oriented Design (OOD)*: Objek, atribut, perilaku (*state & behavior*).
  - Paradigma baru: *Vibe Coding* (Mengapa pemahaman PBO adalah kunci agar AI tidak menghasilkan *spaghetti code*).
- **Referensi Buku**: Chapter 1 (*Object-Oriented Design*)
- **Praktikum Vibe Coding**:
  - Konfigurasi environment (Python 3.10+, VS Code, AI Assistant: Cursor/Antigravity/Copilot).
  - Latihan membedah studi kasus nyata (misal: Sistem Antrean Rumah Sakit) ke dalam daftar entitas objek sebelum menyentuh kode.

##### Minggu 02: Deklarasi Objek, Class, dan Type Hints
- **Materi Teori**:
  - Sintaks class Python: `class`, method, keyword `self`, method inisialisasi `__init__`.
  - Type hints (`int`, `str`, `list[str]`, `Optional`) untuk kejelasan kontrak data.
  - Konvensi PEP 8 untuk penamaan class dan method.
- **Referensi Buku**: Chapter 2 (*Objects in Python*)
- **Praktikum Vibe Coding**:
  - Mahasiswa merancang spesifikasi entitas (misal: `Buku`, `AnggotaPerpus`).
  - Mengarahkan AI meng-generate *skeleton class* ber-type hints, lalu menguji instansiasinya secara interaktif.

##### Minggu 03: Enkapsulasi, Proteksi State, dan Decorator `@property`
- **Materi Teori**:
  - Filosofi privasi data di Python (*consenting adults* vs Java strict private).
  - Penandaan internal: `_protected` dan *name mangling* `__private`.
  - Getter dan Setter yang *Pythonic* menggunakan `@property` dan `@setter`.
  - Validasi *invariants* (mencegah state objek menjadi tidak valid).
- **Referensi Buku**: Chapter 2 (*Objects in Python*) & Chapter 5 (*When to Use OOP*)
- **Praktikum Vibe Coding**:
  - Menantang AI membuat class `RekeningBank` atau `DompetDigital`.
  - Menemukan celah *bug* di mana saldo bisa diubah sembarangan tanpa validasi, lalu memerintahkan AI me-refactor menjadi `@property`.

---

#### 📌 BLOK 2: EMPAT PILAR PBO & ERROR HANDLING

##### Minggu 04: Pewarisan (*Inheritance*) & Hubungan *Is-A*
- **Materi Teori**:
  - Konsep pewarisan (*Generalization & Specialization*).
  - Sintaks inheritance: `class SubClass(SuperClass)`, fungsi `super().__init__()`.
  - Mengganti perilaku method (*Method Overriding*).
  - Kapan harus mewarisi dan kapan inheritance menjadi jebakan (*Fragile Base Class*).
- **Referensi Buku**: Chapter 3 (*When Objects Are Alike*)
- **Praktikum Vibe Coding**:
  - Memodelkan sistem `Pegawai` dengan turunan `Manager`, `Programmer`, dan `Sales`.
  - Mereview kode AI: Mengoreksi pemanggilan `super()` yang terlewat.

##### Minggu 05: Multiple Inheritance & Method Resolution Order (MRO)
- **Materi Teori**:
  - Pewarisan berganda (*Multiple Inheritance*) dan permasalahan *Diamond Problem*.
  - Mekanisme C3 Superclass Linearization & atribut `__mro__`.
  - Desain arsitektur menggunakan **Mixin Pattern** untuk fungsionalitas modular.
- **Referensi Buku**: Chapter 3 (*When Objects Are Alike*)
- **Praktikum Vibe Coding**:
  - Membuat `JSONSerializableMixin` dan `LoggerMixin`.
  - Memerintahkan AI menyematkan mixin pada class bisnis dan menginspeksi urutan MRO via terminal.

##### Minggu 06: Penanganan Error Berorientasi Objek (*Custom Exceptions*)
- **Materi Teori**:
  - Hirarki class Exception bawaan Python (`BaseException` $\rightarrow$ `Exception`).
  - Blok `try - except - else - finally` dan *exception chaining* (`from`).
  - Mendefinisikan class Exception kustom yang membawa data kontekstual.
- **Referensi Buku**: Chapter 4 (*Expecting the Unexpected*)
- **Praktikum Vibe Coding**:
  - Mengganti penggunaan error generik `raise Exception("error")` dari AI menjadi exception spesifik domain: `SaldoTidakCukupError`, `BukuSudahDipinjamError`.

##### Minggu 07: Abstraksi, Abstract Base Classes (ABCs), & Interface
- **Materi Teori**:
  - Konsep Abstraksi: Menyembunyikan kompleksitas dan mendefinisikan kontrak antarmuka.
  - Modul bawaan `abc`: Class `ABC` dan decorator `@abstractmethod`.
  - *Duck Typing* (*informal interface*) vs *Abstract Base Class* (*formal interface*).
- **Referensi Buku**: Chapter 6 (*Abstract Base Classes*)
- **Praktikum Vibe Coding**:
  - Merancang antarmuka `PaymentProcessor` (metode `bayar()` dan `refund()`).
  - Mengarahkan AI mengimplementasikan `TransferBankPayment`, `EWalletPayment`, dan `CreditCardPayment`.
  - Membuktikan bahwa class turunan yang belum mengimplementasikan method abstrak tidak bisa diinstansiasi.

---

#### 📝 MINGGU 08: UJIAN TENGAH SEMESTER (UTS)
- **Bentuk Evaluasi**: Studi Kasus Arsitektur PBO Mandiri.
- **Format**: Mahasiswa diberikan skenario bisnis. Mereka wajib membuat desain Class Diagram, mengarahkan AI untuk implementasi, mendokumentasikan log perbaikan di `PROMPT_LOG.md`, dan menyerahkan kode yang lolos pengujian.

---

#### 📌 BLOK 3: PYTHONIC OOP & STRUKTUR DATA LANJUT

##### Minggu 09: *Magic / Dunder Methods* & *Operator Overloading*
- **Materi Teori**:
  - Protokol objek Python via Dunder (`__init__`, `__str__`, `__repr__`).
  - Operator overloading untuk aritmatika: `__add__`, `__sub__`, `__mul__`.
  - Perbandingan objek: `__eq__`, `__lt__`, `__le__` dan decorator `@total_ordering`.
- **Referensi Buku**: Chapter 6 (*Operator Overloading*)
- **Praktikum Vibe Coding**:
  - Membuat class `Money` atau `Vektor2D` yang bisa dijumlahkan langsung dengan operator `+`, dicetak rapi dengan `print()`, dan dibandingkan nilainya secara otomatis.

##### Minggu 10: Struktur Data Modern & Python Dataclasses
- **Materi Teori**:
  - Mengapa class biasa sering memiliki *boilerplate* repetitif.
  - Modul `dataclasses`: Decorator `@dataclass`, penanganan atribut otomatis, `frozen=True` (immutability).
  - Hook inisialisasi lanjutan: `__post_init__` untuk validasi otomatis.
- **Referensi Buku**: Chapter 7 (*Python Data Structures*)
- **Praktikum Vibe Coding**:
  - Meminta AI me-refactor model class tradisional yang panjang menjadi `@dataclass` yang ramping dan type-safe.

##### Minggu 11: Komposisi vs Pewarisan (*Composition Over Inheritance*)
- **Materi Teori**:
  - Prinsip *"Favor Composition over Inheritance"*.
  - Menghindari hierarki turunan yang terlalu dalam dan kaku.
  - Objek Callable via dunder method `__call__` dan integrasi konsep fungsi ke objek.
- **Referensi Buku**: Chapter 5 (*When to Use OOP*) & Chapter 8 (*FP and OOP*)
- **Praktikum Vibe Coding**:
  - Menemukan *code smell* pada kode rancangan AI yang menyalahgunakan inheritance, lalu memandu AI mengubahnya menjadi sistem komposisi komponen (*has-a*).

##### Minggu 12: Iterator Protocol & Objek Generator
- **Materi Teori**:
  - Protokol iterasi: Dunder `__iter__` dan `__next__`.
  - Perbedaan Iterable vs Iterator.
  - Membangun class generator dengan keyword `yield` untuk efisiensi memori pada dataset besar.
- **Referensi Buku**: Chapter 10 (*The Iterator Pattern*)
- **Praktikum Vibe Coding**:
  - Membangun class `LogFileReader` atau `DataPagination` yang dapat di-looping menggunakan `for item in data:` tanpa me-load seluruh file ke RAM.

---

#### 📌 BLOK 4: DESIGN PATTERNS, TESTING & PROYEK

##### Minggu 13: Creational & Structural Design Patterns
- **Materi Teori**:
  - Pengenalan Gang of Four (GoF) patterns dalam paradigma Pythonic.
  - **Singleton Pattern**: Mengelola resource tunggal (koneksi database / konfigurasi).
  - **Factory Method Pattern**: Menyembunyikan logika instansiasi objek rumit.
  - **Facade & Adapter Pattern**: Menyederhanakan interaksi antarmuka yang kompleks.
- **Referensi Buku**: Chapter 11 & Chapter 12 (*Common & Advanced Design Patterns*)
- **Praktikum Vibe Coding**:
  - Mengarahkan AI mengimplementasikan `ReportExporterFactory` (menghasilkan objek `PDFExporter`, `CSVExporter`, `ExcelExporter`).

##### Minggu 14: Behavioral Design Patterns (Strategy & Observer)
- **Materi Teori**:
  - **Strategy Pattern**: Mengganti algoritma saat runtime tanpa mengubah konteks pemanggil.
  - **Observer Pattern**: Sistem publish-subscribe / event-driven notification antar objek.
- **Referensi Buku**: Chapter 11 (*Common Design Patterns*)
- **Praktikum Vibe Coding**:
  - Membangun sistem transaksi e-commerce: Objek `Cart` mengadopsi diskon dinamis via Strategy Pattern, dan mengirimkan notifikasi status via Observer Pattern.

##### Minggu 15: Automated Unit Testing untuk Sistem OOP (`pytest`)
- **Materi Teori**:
  - Pentingnya pengujian otomatis dalam rekayasa perangkat lunak.
  - Kerangka kerja `pytest`: Assertion, Test Discovery, Test Fixtures untuk inisialisasi objek.
  - Mocking: Menguji method objek tanpa memanggil sistem eksternal nyata.
- **Referensi Buku**: Chapter 13 (*Testing Object-Oriented Programs*)
- **Praktikum Vibe Coding**:
  - Mahasiswa menyusun skenario *test cases*, memerintahkan AI menulis `test_system.py`, lalu memverifikasi seluruh metode class lolos 100% green tests.

---

#### 🎯 MINGGU 16: UJIAN AKHIR SEMESTER (UAS) / SHOWCASE TUGAS BESAR
- **Bentuk Evaluasi**: Presentasi & Demo Proyek Perangkat Lunak Berbasis OOP.
- **Deliverables**:
  1. Repositori Source Code Python yang bersih, modular, dan berorientasi objek (menerapkan minimal 1-2 Design Patterns).
  2. Berkas pengujian otomatis (`pytest`) yang mencakup fungsionalitas inti.
  3. Dokumen **`PROMPT_LOG.md`** yang mendokumentasikan peran mahasiswa sebagai arsitek kode dan validator hasil AI.
  4. Dokumen Arsitektur & Diagram Kelas (UML / Mermaid).

---

### 📊 Komponen Penilaian Semester

| Komponen | Bobot | Deskripsi |
| :--- | :---: | :--- |
| **Praktikum & Log Mingguan** | 25% | Kualitas pengujian mingguan dan catatan `PROMPT_LOG.md` |
| **Kuis / Tugas Analisis OOD** | 15% | Analisis desain objek, diagram kelas, dan code smell review |
| **Ujian Tengah Semester (UTS)** | 25% | Ujian studi kasus mandiri (pemodelan pilar PBO) |
| **Tugas Besar & UAS** | 35% | Proyek akhir aplikasi OOP lengkap + Unit Test + Presentasi |
