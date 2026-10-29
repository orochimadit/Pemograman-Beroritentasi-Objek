# 📘 Modul 13: Creational & Structural Design Patterns (Factory & Facade)

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami konsep pola desain perangkat lunak (*Software Design Patterns*) klasik GoF (*Gang of Four*).
2. Mengimplementasikan **Factory Method Pattern** untuk memisahkan logika instansiasi objek rumit dari kode pemanggil.
3. Menerapkan prinsip *Open/Closed Principle (OCP)*: Terbuka untuk penambahan fitur baru, tertutup untuk modifikasi kode lama.
4. Mengimplementasikan **Facade Pattern** untuk menyederhanakan interaksi dengan banyak subsistem yang kompleks.

---

## 1. Factory Method Pattern (Pola Pembuatan Objek)

### Masalah Tanpa Factory:
Jika kode pemanggil (*client*) melakukan instansiasi langsung dengan banyak `if-elif-else`:
```python
# ❌ Rawan bug: Klien harus tahu nama setiap class konkret
if format == "pdf":
    exporter = PDFExporter()
elif format == "excel":
    exporter = ExcelExporter()
# Jika ada format baru, kita harus mengedit dan menguji ulang kode klien ini!
```

### Solusi Factory Method:
Klien hanya meminta objek ke *Factory*, dan *Factory* yang bertanggung jawab memilih serta membuatkan instance class yang tepat.

```
+--------------------+            meminta objek            +------------------------+
|    KODE CLIENT     | ──────────────────────────────────> | ExportFactory.create() |
+--------------------+                                     +------------------------+
          ▲                                                             │
          │ menggunakan antarmuka seragam                              ▼ menghasilkan
          └───────────────────────────────────────────────── [ PDF / Excel / CSV ]
```

---

## 2. Facade Pattern (Pola Penyederhanaan Antarmuka)

Facade menyediakan antarmuka tingkat tinggi tunggal yang membungkus banyak class subsistem rumit di baliknya, sehingga klien cukup memanggil satu method praktis.

```
                            [ KODE KLIEN ]
                                  │
                                  ▼ cukup panggil: facade.daftar_yudisium(nim)
                    ┌───────────────────────────┐
                    │    PORTAL AKADEMIK FACADE │
                    └───────────────────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        ▼                         ▼                         ▼
[ Subsistem SPP ]        [ Subsistem Skripsi ]    [ Subsistem Notifikasi ]
```

---

## 3. Studi Kasus Demo: Factory Ekspor Laporan

```python
from abc import ABC, abstractmethod

class DocumentExporter(ABC):
    @abstractmethod
    def export(self, data: list[dict]) -> None:
        pass

class PDFExporter(DocumentExporter):
    def export(self, data: list[dict]) -> None:
        print(f"[PDF]: Mengekspor {len(data)} baris data ke file dokumen laporan.pdf...")

class ExcelExporter(DocumentExporter):
    def export(self, data: list[dict]) -> None:
        print(f"[EXCEL]: Menyusun {len(data)} baris data ke spreadsheet workbook.xlsx...")

class CSVExporter(DocumentExporter):
    def export(self, data: list[dict]) -> None:
        print(f"[CSV]: Menulis {len(data)} record ke file teks data.csv...")


class ExporterFactory:
    """Factory Class terpusat"""
    _registry: dict[str, type[DocumentExporter]] = {
        "pdf": PDFExporter,
        "excel": ExcelExporter,
        "csv": CSVExporter,
    }

    @classmethod
    def get_exporter(cls, format_type: str) -> DocumentExporter:
        exporter_class = cls._registry.get(format_type.lower())
        if not exporter_class:
            raise ValueError(f"Format '{format_type}' tidak didukung! Pilihan: {list(cls._registry.keys())}")
        return exporter_class()


# Demo Klien
if __name__ == "__main__":
    dummy_data = [{"id": 1, "nama": "A"}, {"id": 2, "nama": "B"}]

    # Klien cukup menyebutkan string formatnya, tanpa perlu tahu implementasi class PDF/Excel
    pengekspor = ExporterFactory.get_exporter("pdf")
    pengekspor.export(dummy_data)
```

---

## 4. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Facade Portal Yudisium Mahasiswa
1. **Buat 3 Subsistem Terpisah**:
   - `KeuanganService`: Method `cek_tunggakan_spp(nim: str) -> bool`.
   - `PerpustakaanService`: Method `cek_bebas_pinjaman(nim: str) -> bool`.
   - `AkademikService`: Method `validasi_transkrip_skripsi(nim: str) -> bool`.
2. **Buat Class `PendaftaranYudisiumFacade`**:
   - Method utama: `proses_yudisium(nim: str) -> str`.
   - Di dalam method ini, panggil ketiga subsistem di atas. Jika semua bernilai `True`, kembalikan `"SELAMAT, PENDAFTARAN YUDISIUM DITERIMA"`. Jika ada yang gagal, jelaskan syarat mana yang belum terpenuhi.
3. **Instruksi Vibe Coding**:
   - Arahkan AI membuat pola Facade ini.
   - Uji kode klien agar kode klien sama sekali tidak berinteraksi langsung dengan class `KeuanganService` atau `PerpustakaanService`.
   - Lampirkan screenshot keberhasilan eksekusi di `PROMPT_LOG.md`.
