# 📚 PANDUAN LENGKAP TUGAS IN-LAB & TAKE-HOME MINGGUAN
## MATA KULIAH: PEMROGRAMAN BERORIENTASI OBJEK (PBO)
### Pendekatan: Modern Python & Vibe Coding Framework

---

Setiap pertemuan perkuliahan PBO memiliki **dua jenis penugasan**:
1. **🧪 Tugas In-Lab (Tugas Kelas / Hands-on di Lab, 30–45 Menit)**:
   - Dilakukan langsung saat jam praktikum.
   - Menggunakan model hibrida: menulis kode skeleton manual 15 menit, lalu mengarahkan AI (Antigravity/Cursor) untuk refactoring dan pengujian.
   - Dinilai atau dicek langsung (*uji petik*) oleh dosen/asisten lab di tempat.
2. **🏠 Tugas Take-Home (Tugas Mandiri Mingguan / Proyek Mini)**:
   - Dikerjakan secara mandiri di luar jam kuliah.
   - Wajib menyertakan file kode Python, file test `pytest`, dan dokumen **`PROMPT_LOG.md`**.
   - Dikumpulkan ke LMS (Google Classroom/Moodle) maksimal **H-1 sebelum pertemuan berikutnya**.

---

### MINGGU 01: Paradigma PBO vs Prosedural & Setup Vibe Coding
* **Materi**: Pengantar PBO, Paradigma Vibe Coding, State & Behavior.
* **🧪 Tugas In-Lab (Kelas)**:
  - Buka editor tanpa AI (15 menit). Tulis manual 2 fungsi prosedural untuk antrean pasien klinik yang memanipulasi dictionary.
  - Aktifkan AI di Antigravity (20 menit). Minta AI mengubah kode prosedural tadi menjadi class `Pasien` dan `AntreanKlinik`. Mahasiswa mengaudit: apakah ada data yang bocor di luar class?
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Manajemen Menu & Pesanan Kafe*.
  - Rancang 3 class: `ItemMenu`, `Pesanan`, dan `MejaKafe`.
  - Gunakan AI untuk membuat prototype awal, lakukan minimal 2 kali revisi prompt untuk memastikan data pesanan terhitung akurat. Kumpulkan file `kafe_app.py` dan `PROMPT_LOG.md`.

---

### MINGGU 02: Objek, Class, State & Behavior, dan Type Hints
* **Materi**: Constructor `__init__`, Parameter `self`, Type Annotations (PEP 484), Instance vs Class Attributes.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual class `Buku` dengan 4 atribut dan method `pinjam()`.
  - Minta AI menambahkan class attribute `total_buku_tersedia` yang berkurang saat dipinjam dan bertambah saat dikembalikan.
  - Verifikasi: Apakah nilai class attribute konsisten diakses lewat `Buku.total_buku_tersedia`?
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Rental Kendaraan Kampus*.
  - Buat class `Kendaraan` dan `Pelanggan` dengan Type Hints ketat (`plat_nomor: str`, `harga_per_hari: float`, `sewaan_aktif: list[Kendaraan]`).
  - Buat method `tampilkan_invoice(hari: int) -> float`. Kumpulkan `rental_app.py` dan `PROMPT_LOG.md`.

---

### MINGGU 03: Enkapsulasi, Proteksi State, & Decorator `@property`
* **Materi**: Konvensi `_protected`, `__private`, `@property`, `@<nama>.setter`, Validasi Invariant.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual class `RekeningBank` dengan atribut `_saldo`.
  - Minta AI menerapkan decorator `@property` dan setter dengan validasi `if nilai < 0: raise ValueError`.
  - *Break the code*: Teman sebelah mencoba memasukkan saldo minus dan mengecek apakah program melempar error validasi.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Nilai Akademik & Transkrip Mahasiswa*.
  - Class `NilaiMatkul`: setter memvalidasi nilai angka (0 - 100).
  - Buat **read-only property** `nilai_huruf` (A/B/C/D/E) dan `status_lulus` yang terkalkulasi otomatis secara real-time tanpa bisa dimanipulasi dari luar. Kumpulkan `transkrip_app.py` dan `PROMPT_LOG.md`.

---

### MINGGU 04: Pewarisan (*Inheritance*), `super()`, & Method Overriding
* **Materi**: Generalisasi & Spesialisasi, Hirarki Pewarisan, Fungsi `super()`, Method Overriding.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual base class `Karyawan` dengan method `hitung_gaji()`.
  - Minta AI membuat 2 subclass: `KaryawanTetap` dan `KaryawanKontrak`.
  - Lakukan audit kode AI: Pastikan constructor subclass memanggil `super().__init__(...)` dan tidak menduplikasi assignment atribut parent.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Tiket Transportasi Multi-Moda*.
  - Base class `TiketPerjalanan`. Subclass `TiketPesawat` (ada biaya bagasi & airport tax) dan `TiketKereta` (diskon lansia/pelajar).
  - Override method `hitung_total_bayar()`. Kumpulkan `tiket_app.py` dan `PROMPT_LOG.md`.

---

### MINGGU 05: Multiple Inheritance, Diamond Problem, & Mixin Pattern
* **Materi**: Multiple Inheritance di Python, C3 Linearization, Atribut `__mro__`, Mixin Pattern.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual `TimestampMixin` dan `JSONExportMixin`.
  - Pasang kedua mixin tersebut pada class `Produk`.
  - Jalankan perintah `print(Produk.__mro__)` di terminal dan amati urutan resolusi method Python.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Entitas E-Commerce Berfitur Tracking*.
  - Buat `AuditLogMixin` dan `SoftDeleteMixin` (fitur `is_deleted = True` dan `deleted_at`).
  - Pasang pada entitas `Pengguna` dan `KuponDiskon`. Kumpulkan `ecommerce_mixins.py` dan `PROMPT_LOG.md`.

---

### MINGGU 06: Penanganan Error Berorientasi Objek (*Custom Exceptions*)
* **Materi**: Hirarki Exception, `try-except-finally`, `raise ... from ...`, Objek Error Berisi Metadata.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual class `ATMError(Exception)` dan `SaldoTidakCukupError(ATMError)` yang menyimpan atribut `saldo_aktif` dan `jumlah_tarik`.
  - Minta AI menyimulasikan transaksi ATM. Tangkap error dengan `except SaldoTidakCukupError as e:` dan cetak info selisih kekurangannya.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Reservasi Kamar Hotel*.
  - Buat hirarki custom exception: `KamarTidakTersediaError`, `DurasiMenginapInvalidError`, `KapasitasMelebihiBatasError`.
  - Terapkan pada class `ReservasiHotel`. Kumpulkan `hotel_exceptions.py` dan `PROMPT_LOG.md`.

---

### MINGGU 07: Abstraksi, Abstract Base Classes (ABCs), & Interface
* **Materi**: Modul `abc`, `@abstractmethod`, Formal Interface, Dependency Inversion.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual `PaymentProcessor(ABC)` dengan method abstrak `bayar()` dan `refund()`.
  - Minta AI membuat turunan `MidtransPayment` dan `TransferManual`.
  - Hapus sengaja method `refund()` pada salah satu turunan, lalu run untuk melihat pesan error `TypeError: Can't instantiate abstract class`.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Ekspedisi Multi-Kurir*.
  - Buat `EkspedisiBase(ABC)` dengan method abstrak `hitung_ongkir()` dan `lacak_resi()`.
  - Implementasikan pada 3 class kurir: `JNEExpress`, `SiCepatService`, dan `PosIndonesia`. Kumpulkan `ekspedisi_abc.py` dan `PROMPT_LOG.md`.

---

### MINGGU 08: UTS (Evaluasi Tengah Semester)
* **🧪 Evaluasi In-Lab (3 Jam Mandiri)**:
  - Live Case: *Core Auction Engine (Sistem Lelang Online)*.
  - Mahasiswa mendesain Class Diagram, mengarahkan AI membangun modul terenkapsulasi dengan ABC dan Custom Exception, merevisi bug AI, dan menjalani wawancara lisan 2 menit dengan dosen.
* **🏠 Tugas Take-Home**:
  - *Tidak ada tugas rumah (Masa Evaluasi Tengah Semester)*.

---

### MINGGU 09: Magic / Dunder Methods & Operator Overloading
* **Materi**: Dunder Methods (`__str__`, `__repr__`, `__eq__`, `__add__`, `__len__`, `__getitem__`).
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual class `Money` dengan atribut `amount` dan `currency`.
  - Implementasikan `__add__` agar dua objek `Money` bisa dijumlahkan langsung dengan operator `+`.
  - Verifikasi: Jika valuta berbeda (USD vs IDR), lemparkan `ValueError`.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Keranjang Belanja Pintar (`ShoppingCart`)*.
  - Implementasikan `__len__` (total item), `__getitem__` (akses `cart[0]`), `__contains__` (`if "Item" in cart`), dan operator `+` untuk menggabungkan dua keranjang. Kumpulkan `smart_cart.py` dan `PROMPT_LOG.md`.

---

### MINGGU 10: Struktur Data Modern & Python Dataclasses
* **Materi**: `@dataclass`, `frozen=True` (immutability), `field(default_factory=...)`, Hook `__post_init__`.
* **🧪 Tugas In-Lab (Kelas)**:
  - Bandingkan class reguler 25 baris dengan `@dataclass` 6 baris.
  - Tambahkan parameter `frozen=True` pada objek `Alamat` dan buktikan bahwa atributnya tidak bisa diubah setelah diinstansiasi.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Tiket Konser & Seat Map*.
  - Buat `@dataclass(frozen=True)` untuk `Seat` dan `@dataclass` untuk `TiketKonser`.
  - Tambahkan validasi batas harga minimum kategori VIP di dalam method `__post_init__`. Kumpulkan `tiket_dataclass.py` dan `PROMPT_LOG.md`.

---

### MINGGU 11: Komposisi vs Pewarisan (*Composition Over Inheritance*)
* **Materi**: Prinsip *"Favor Composition over Inheritance"*, Relasi *Has-A*, Menghindari Subclass Explosion.
* **🧪 Tugas In-Lab (Kelas)**:
  - Dosen menampilkan kode RPG yang buruk dengan hierarki turunan bertingkat (`Hero` $\rightarrow$ `Mage` $\rightarrow$ `FlyingMage`).
  - Minta AI me-refactor menjadi komposisi komponen: `Hero` memiliki `WeaponBehavior` dan `MovementBehavior`. Mahasiswa menguji fleksibilitas ganti senjata saat runtime.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Perakit Komputer Custom (PC Builder)*.
  - Rancang class `Komputer` yang tersusun atas komponen terpisah: `Processor`, `RAM`, `GPU`, dan `PowerSupply`.
  - Buat kalkulasi kebutuhan watt total dan pengecekan kelayakan daya PSU. Kumpulkan `pc_builder.py` dan `PROMPT_LOG.md`.

---

### MINGGU 12: Iterator Protocol & Generator Objects
* **Materi**: Dunder `__iter__` dan `__next__`, Keyword `yield`, Generator Function, Efisiensi Memori (Lazy Evaluation).
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual class `LogFileIterator` yang membaca file teks baris demi baris menggunakan `readline()`.
  - Gunakan `sys.getsizeof` untuk mengamati konsumsi memori.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Paginasi Katalog Produk (E-Commerce Paginator)*.
  - Buat class `ProductCatalogStream` yang mampu mengiterasi 100.000 data dummy secara *lazy* (chunk per 20 produk) tanpa kehabisan RAM. Kumpulkan `paginator.py` dan `PROMPT_LOG.md`.

---

### MINGGU 13: Creational & Structural Patterns (Factory & Facade)
* **Materi**: Gang of Four (GoF) Patterns, Factory Method Pattern, Open/Closed Principle, Facade Pattern.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual `DocumentExporter(ABC)` dengan turunan `PDFExporter` dan `ExcelExporter`.
  - Minta AI membuat class `ExporterFactory` dengan dictionary registry. Uji pemanggilan ekspor dokumen secara dinamis.
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Facade Portal Yudisium Mahasiswa*.
  - Bangun 3 subsistem terpisah (`KeuanganService`, `PerpustakaanService`, `AkademikService`).
  - Buat class `PendaftaranYudisiumFacade` yang menyediakan satu method sederhana `daftar_yudisium(nim)`. Kumpulkan `yudisium_facade.py` dan `PROMPT_LOG.md`.

---

### MINGGU 14: Behavioral Patterns (Strategy & Observer)
* **Materi**: Strategy Pattern (Algoritma Dinamis), Observer Pattern (Publish-Subscribe & Event-Driven).
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual keranjang belanja dengan `DiskonStrategy(ABC)`.
  - Buat subclass `DiskonVIP` dan `DiskonFlashSale`. Uji coba penggantian strategi diskon saat runtime (`cart.set_strategi(...)`).
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Sistem Pemantau Harga Kripto (Observer Pattern)*.
  - Subject `CryptoPriceSubject` memberitahu secara otomatis kepada observer `TelegramAlertObserver` dan `PriceLoggerObserver` saat harga koin berubah. Kumpulkan `crypto_observer.py` dan `PROMPT_LOG.md`.

---

### MINGGU 15: Automated Unit Testing untuk Sistem PBO (`pytest`)
* **Materi**: Filosofi Testing, Fixture `@pytest.fixture`, Pengujian Exception `pytest.raises`, TDD Loop.
* **🧪 Tugas In-Lab (Kelas)**:
  - Ketik manual file `wallet.py`.
  - Buat file `test_wallet.py` berisi 4 test cases dengan `pytest`.
  - Jalankan `pytest -v` di terminal hingga semua indikator berstatus hijau (*PASSED*).
* **🏠 Tugas Take-Home (Rumah)**:
  - *Studi Kasus: Test Suite Komprehensif Sistem Penjualan*.
  - Susun minimal 8 *test cases* otomatis yang menguji validasi setter, polimorfisme, dan diskon strategy. Kumpulkan `test_penjualan.py` dan `PROMPT_LOG.md`.

---

### MINGGU 16: UAS & Showcase Proyek Akhir
* **🧪 Evaluasi In-Lab (Kelas)**:
  - Demo Presentasi Langsung Proyek Akhir Sistem PBO (Aplikasi + 2 Design Patterns + Minimal 10 Test Cases `pytest` + `PROMPT_LOG.md`).
* **🏠 Tugas Take-Home**:
  - *Penutupan Semester & Pengumpulan Final Repositori*.
