# 📘 Modul 06: Penanganan Error Berorientasi Objek (*Custom Exceptions*)

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami bahwa Exception di Python adalah **objek** turunan dari class `BaseException`.
2. Merancang hierarki *Custom Exception* berbasis domain aplikasi.
3. Menggunakan struktur `try - except - else - finally` dan teknik *Exception Chaining* (`raise ... from ...`).
4. Menyimpan data kontekstual di dalam objek Exception untuk mempermudah *debugging*.

---

## 1. Exception Sebagai Objek

Di Python, seluruh error adalah objek yang diturunkan dari class `Exception`.

```
                    BaseException
                          ▲
                          │
                      Exception
                          ▲
        ┌─────────────────┴─────────────────┐
        │                                   │
   StandardError                     AplikasiDomainError
(ValueError, TypeError, etc.)      (Custom Exception Kita)
                                            ▲
                          ┌─────────────────┴─────────────────┐
                          │                                   │
                  SaldoTidakCukupError                PINSalahError
```

### Mengapa Harus Membuat Custom Exception?
Bandingkan dua gaya penanganan error berikut:
```python
# ❌ Buruk: Menggunakan Exception generic bawaan
raise Exception("Saldo tidak cukup")

# ✅ Sangat Baik: Objek error spesifik domain yang membawa metadata
raise SaldoTidakCukupError(saldo_aktif=100000, jumlah_tarik=250000)
```

---

## 2. Studi Kasus Demo: Mesin ATM Berorientasi Objek

```python
class ATMError(Exception):
    """Base Exception untuk seluruh masalah operasional ATM"""
    pass


class SaldoTidakCukupError(ATMError):
    """Dipicu saat nasabah menarik uang melebihi saldo rekening"""
    def __init__(self, saldo_aktif: float, jumlah_tarik: float) -> None:
        self.saldo_aktif = saldo_aktif
        self.jumlah_tarik = jumlah_tarik
        self.selisih = jumlah_tarik - saldo_aktif
        pesan = (
            f"Penarikan gagal! Saldo Anda: Rp {saldo_aktif:,.2f}, "
            f"diminta: Rp {jumlah_tarik:,.2f} (Kurang: Rp {self.selisih:,.2f})"
        )
        super().__init__(pesan)


class BatasHarianTerlampauiError(ATMError):
    """Dipicu jika penarikan melebihi limit harian ATM"""
    def __init__(self, limit_maksimal: float) -> None:
        pesan = f"Transaksi ditolak! Maksimal penarikan harian adalah Rp {limit_maksimal:,.2f}"
        super().__init__(pesan)


class RekeningBank:
    LIMIT_HARIAN = 5_000_000.0

    def __init__(self, no_rek: str, nama: str, saldo_awal: float) -> None:
        self.no_rek = no_rek
        self.nama = nama
        self.saldo = saldo_awal
        self.total_ditarik_hari_ini = 0.0

    def tarik_tunai(self, nominal: float) -> None:
        if nominal + self.total_ditarik_hari_ini > self.LIMIT_HARIAN:
            raise BatasHarianTerlampauiError(self.LIMIT_HARIAN)

        if nominal > self.saldo:
            raise SaldoTidakCukupError(saldo_aktif=self.saldo, jumlah_tarik=nominal)

        self.saldo -= nominal
        self.total_ditarik_hari_ini += nominal
        print(f"Penarikan Rp {nominal:,.2f} sukses. Sisa saldo: Rp {self.saldo:,.2f}")


# Pengujian Program dengan Try-Except
if __name__ == "__main__":
    rek = RekeningBank("123-456", "Budi", saldo_awal=1_000_000)

    try:
        rek.tarik_tunai(1_500_000)
    except SaldoTidakCukupError as e:
        print(f"[LOG KASIR]: {e}")
        print(f"Info tambahan: Uang kurang sebesar Rp {e.selisih:,.2f}")
    except ATMError as e:
        print(f"[ERROR UMUM ATM]: {e}")
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Reservasi Kamar Hotel
1. **Rancang Hirarki Exception**:
   - `HotelBookingError(Exception)` (Induk)
     - `KamarTidakTersediaError` (atribut: `tipe_kamar: str`, `tanggal: str`)
     - `DurasiMenginapInvalidError` (atribut: `check_in: str`, `check_out: str`)
     - `KapasitasMelebihiBatasError` (atribut: `jumlah_tamu: int`, `maks_kapasitas: int`)
2. **Buat Class `ReservasiHotel`**:
   - Method `pesan_kamar(tipe: str, jumlah_tamu: int, tgl_checkin, tgl_checkout)`.
   - Lemparkan exception yang sesuai jika aturan kamar dilanggar.
3. **Instruksi Vibe Coding**:
   - Instruksikan AI untuk membangun logic di atas.
   - **Tinjau Kode AI**: Pastikan AI tidak menulis `raise Exception(...)` generik. Semua error wajib menggunakan class custom yang diturunkan dari `HotelBookingError`.
   - Dokumentasikan contoh try-except penanganannya di `PROMPT_LOG.md`.
