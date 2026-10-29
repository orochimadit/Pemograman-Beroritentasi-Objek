# 📝 Panduan Evaluasi Tengah Semester (UTS)
## MATA KULIAH: PEMROGRAMAN BERORIENTASI OBJEK (PBO)

---

### 🎯 Tujuan Evaluasi
Mengukur kemampuan mahasiswa dalam:
1. Memodelkan sistem dunia nyata ke dalam diagram class dan arsitektur objek.
2. Mengintegrasikan 4 Pilar PBO (Enkapsulasi, Inheritance, Polimorfisme, Abstraksi).
3. Menggunakan metode Vibe Coding secara terstruktur (architectural prompting, code review, dan deteksi kelemahan AI).

---

### 💼 Skenario Studi Kasus: "Sistem Manajemen Lelang Online (AutoBid)"

Sebuah startup ingin membangun inti sistem lelang online (*Core Auction Engine*). Anda ditugaskan sebagai **Lead Software Architect** untuk merancang dan memverifikasi modul PBO sistem ini.

#### 📋 Kebutuhan Fungsional Sistem:
1. **Model Objek Barang Lelang (`BarangLelang`)**:
   - Memiliki atribut: `id_barang`, `nama`, `deskripsi`, `harga_awal`, dan status lelang (`DRAFT`, `BERJALAN`, `SELESAI`).
   - Terapkan enkapsulasi: Penawaran (*bid*) terbaru harus selalu lebih tinggi dari penawaran tertinggi sebelumnya. Jika tidak, tolak dengan Custom Exception.
2. **Hirarki Penawar Lelang (Inheritance & Polymorphism)**:
   - Base Class: `PesertaLelang` (atribut: `id_peserta`, `nama`, `saldo_deposit`).
   - Subclass 1: `PesertaReguler`: Maksimal menawar dengan nominal saldo deposit yang dimiliki.
   - Subclass 2: `PesertaVIP`: Mendapatkan limit kredit tambahan 20% di atas saldo depositnya.
3. **Penyedia Notifikasi (Abstraction & ABC)**:
   - Buat abstract class `NotifikasiBase(ABC)` dengan method abstrak `kirim_pesan(pesan: str) -> None`.
   - Implementasikan class konkret `EmailNotifikasi` dan `WhatsAppNotifikasi`.
4. **Custom Exception**:
   - `LelangError(Exception)`
     - `PenawaranTerlaluRendahError`
     - `DepositTidakCukupError`
     - `LelangSudahTutupError`

---

### 📦 Berkas yang Wajib Dikumpulkan:
1. `arsitektur_desain.md`: Diagram class (format teks/Mermaid) dan deskripsi pembagian tanggung jawab objek.
2. `core_auction.py`: Kode program Python lengkap (ber-type hints dan PEP 8).
3. `PROMPT_LOG.md`: Catatan minimal 3 siklus percakapan dengan AI (Prompt awal $\rightarrow$ Identifikasi bug/code smell buatan AI $\rightarrow$ Instruksi refactoring).

### 📊 Rubrik Penilaian UTS (Skala 100):
- **Desain & Pemodelan Objek (25%)**: Kebenaran relasi class (*is-a* vs *has-a*) dan penerapan ABC.
- **Enkapsulasi & Proteksi State (20%)**: Penggunaan `@property` dan penolakan manipulasi state tidak sah.
- **Pewarisan & Polimorfisme (20%)**: Kebenaran penggunaan `super()` dan overriding method yang tepat.
- **Error Handling Domain (15%)**: Ketepatan pembuatan dan penanganan custom exception.
- **Dokumentasi Vibe Coding & Review (20%)**: Kualitas analisis mahasiswa terhadap kode yang dihasilkan AI di `PROMPT_LOG.md`.
