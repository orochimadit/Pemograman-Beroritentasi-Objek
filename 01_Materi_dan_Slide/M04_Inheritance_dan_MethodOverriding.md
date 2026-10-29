# 📘 Modul 04: Pewarisan (*Inheritance*), `super()`, & Method Overriding

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami konsep pilar kedua PBO: **Pewarisan (*Inheritance*)** dan hubungan *Is-A*.
2. Menggunakan fungsi `super()` untuk memanggil constructor dan method milik parent class.
3. Melakukan *Method Overriding* untuk mengubah perilaku method di subclass.
4. Menghindari duplikasi kode (*DRY - Don't Repeat Yourself*) antar class terkait.

---

## 1. Konsep Dasar Pewarisan

Pewarisan memungkinkan suatu class (*SubClass / Child Class*) mewarisi atribut dan perilaku dari class lain (*SuperClass / Parent Class*).

```
         +---------------------------------------+
         |               KARYAWAN                |
         |  - id_karyawan: str                   |
         |  - nama: str                          |
         |  - gaji_pokok: float                  |
         |  + hitung_gaji_bulanan() -> float     |
         +---------------------------------------+
                            ▲
                            | (extends / mewarisi)
            +---------------+---------------+
            |                               |
+--------------------------+    +--------------------------+
|      KARYAWAN TETAP      |    |     KARYAWAN KONTRAK     |
|  - tunjangan: float      |    |  - upah_lembur: float    |
|  - bonus_kinerja: float  |    |  - jam_lembur: int       |
|  + override hitung_gaji()|    |  + override hitung_gaji()|
+--------------------------+    +--------------------------+
```

---

## 2. Studi Kasus Demo: Sistem Penggajian Karyawan

```python
class Karyawan:
    def __init__(self, id_karyawan: str, nama: str, gaji_pokok: float) -> None:
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def hitung_gaji_bulanan(self) -> float:
        """Method dasar yang akan dioverride oleh anak-anaknya"""
        return self.gaji_pokok

    def cetak_slip_gaji(self) -> None:
        total = self.hitung_gaji_bulanan()
        print(f"[{self.id_karyawan}] {self.nama} -> Total Gaji: Rp {total:,.2f}")


class KaryawanTetap(Karyawan):
    def __init__(
        self,
        id_karyawan: str,
        nama: str,
        gaji_pokok: float,
        tunjangan_kesehatan: float,
        bonus_tahunan: float = 0.0
    ) -> None:
        # Panggil constructor parent class
        super().__init__(id_karyawan, nama, gaji_pokok)
        self.tunjangan_kesehatan = tunjangan_kesehatan
        self.bonus_tahunan = bonus_tahunan

    def hitung_gaji_bulanan(self) -> float:
        """Override method parent: Gaji pokok + tunjangan"""
        return self.gaji_pokok + self.tunjangan_kesehatan


class KaryawanKontrak(Karyawan):
    def __init__(
        self,
        id_karyawan: str,
        nama: str,
        upah_per_jam: float,
        total_jam_kerja: int
    ) -> None:
        # Gaji pokok diisi 0 karena berbasis jam kerja
        super().__init__(id_karyawan, nama, gaji_pokok=0.0)
        self.upah_per_jam = upah_per_jam
        self.total_jam_kerja = total_jam_kerja

    def hitung_gaji_bulanan(self) -> float:
        """Override method parent: Total jam kerja x tarif per jam"""
        return self.upah_per_jam * self.total_jam_kerja


# Demo Eksekusi Polimorfik
if __name__ == "__main__":
    tim_karyawan: list[Karyawan] = [
        KaryawanTetap("EMP-01", "Budi Santoso", gaji_pokok=6_000_000, tunjangan_kesehatan=1_000_000),
        KaryawanKontrak("EMP-02", "Doni Prasetyo", upah_per_jam=50_000, total_jam_kerja=160),
        KaryawanTetap("EMP-03", "Siti Aminah", gaji_pokok=7_500_000, tunjangan_kesehatan=1_200_000),
    ]

    print("=== SLIP PENGGAJIAN BULANAN ===")
    for k in tim_karyawan:
        # Polimorfisme: memanggil method yang sama, tapi perilaku berbeda tergantung instance objek
        k.cetak_slip_gaji()
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Tiket Transportasi Multi-Moda
1. **Rancang Base Class `TiketPerjalanan`**:
   - Atribut: `kode_tiket: str`, `nama_penumpang: str`, `asal: str`, `tujuan: str`, `harga_dasar: float`.
   - Method: `hitung_total_bayar() -> float` (mengembalikan `harga_dasar`).
2. **Buat Subclass 1: `TiketPesawat`**:
   - Tambah atribut: `berat_bagasi_kg: float`, `pajak_bandara: float = 50_000`.
   - Ketentuan bagasi: Jika `berat_bagasi_kg > 20`, setiap kelebihan kg dikenakan biaya tambahan Rp 25.000.
   - Override `hitung_total_bayar()`.
3. **Buat Subclass 2: `TiketKereta`**:
   - Tambah atribut: `tipe_gerbong: str` ("Eksekutif", "Bisnis", "Ekonomi").
   - Jika "Eksekutif", harga tiket ditambah 40%. Jika "Bisnis", ditambah 20%.
   - Override `hitung_total_bayar()`.
4. **Instruksi Vibe Coding**:
   - Buat prompt agar AI mengimplementasikan skema di atas.
   - Periksa apakah AI menduplikasi assignment atribut `kode_tiket`, `nama_penumpang`, dll di subclass. Jika ya, paksa AI untuk memakai `super().__init__(...)`.
   - Dokumentasikan log interaksi di `PROMPT_LOG.md`.
