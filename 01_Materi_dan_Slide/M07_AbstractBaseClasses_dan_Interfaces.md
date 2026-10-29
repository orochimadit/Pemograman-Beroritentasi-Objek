# 📘 Modul 07: Abstraksi, Abstract Base Classes (ABCs), & Interface

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami konsep pilar keempat PBO: **Abstraksi (*Abstraction*)** dan pembuatan antarmuka (*Interface Contract*).
2. Menggunakan modul bawaan `abc`, class `ABC`, dan decorator `@abstractmethod`.
3. Memahami mengapa class abstrak tidak bisa diinstansiasi secara langsung.
4. Menerapkan prinsip *Dependency Inversion* (bergantung pada abstraksi, bukan implementasi konkret).

---

## 1. Konsep Abstraksi & Interface di Python

Abstraksi memisahkan **APA yang harus dilakukan (*what it does*)** dari **BAGAIMANA cara melakukannya (*how it does it*)**.

```
              << Abstract Base Class >>
                 PaymentProcessor (ABC)
          +-----------------------------------+
          | + bayar(nominal: float) [abstract]|
          | + refund(id_trx: str)   [abstract]|
          +-----------------------------------+
                            ▲
                            │ (implements contract)
           ┌────────────────┴────────────────┐
           │                                 │
+-----------------------+        +-----------------------+
|  MidtransProcessor    |        |    XenditProcessor    |
| + bayar() [konkret]   |        | + bayar() [konkret]   |
| + refund() [konkret]  |        | + refund() [konkret]  |
+-----------------------+        +-----------------------+
```

Jika ada class turunan yang lupa mengimplementasikan salah satu method abstrak, Python akan menolak program dengan pesan:
`TypeError: Can't instantiate abstract class SubClass with abstract method ...`

---

## 2. Studi Kasus Demo: Gerbang Pembayaran (*Payment Gateway*)

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract Base Class yang bertindak sebagai Kontrak Antarmuka"""
    
    @abstractmethod
    def bayar(self, nominal: float) -> bool:
        """Wajib diimplementasikan oleh setiap penyedia pembayaran"""
        pass

    @abstractmethod
    def refund(self, id_transaksi: str) -> bool:
        """Wajib diimplementasikan untuk proses pengembalian dana"""
        pass


class MidtransPayment(PaymentProcessor):
    def bayar(self, nominal: float) -> bool:
        print(f"[MIDTRANS]: Memproses pembayaran QRIS/Gopay sebesar Rp {nominal:,.2f} ... Sukses!")
        return True

    def refund(self, id_transaksi: str) -> bool:
        print(f"[MIDTRANS]: Mengembalikan dana untuk transaksi {id_transaksi} ... Sukses!")
        return True


class TransferBankManual(PaymentProcessor):
    def bayar(self, nominal: float) -> bool:
        print(f"[MANUAL BANK]: Menunggu bukti transfer struk sebesar Rp {nominal:,.2f} ... Terverifikasi!")
        return True

    def refund(self, id_transaksi: str) -> bool:
        print(f"[MANUAL BANK]: Transfer manual balik dana ke rekening nasabah {id_transaksi}.")
        return True


# Fungsi Level Tinggi (High-Level Module) yang Hanya Bergantung pada Abstraksi
def proses_checkout_belanja(processor: PaymentProcessor, total_tagihan: float) -> None:
    print("\n--- MEMULAI PROSES CHECKOUT ---")
    processor.bayar(total_tagihan)
    print("Pesanan diproses dan diteruskan ke bagian pengemasan.")


# Demo Eksekusi
if __name__ == "__main__":
    qris = MidtransPayment()
    bca = TransferBankManual()

    proses_checkout_belanja(qris, 150_000)
    proses_checkout_belanja(bca, 500_000)
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Ekspedisi & Kalkulator Ongkos Kirim
1. **Buat Abstract Base Class `EkspedisiBase(ABC)`**:
   - `@abstractmethod def hitung_ongkir(self, berat_kg: float, jarak_km: float) -> float`: pass
   - `@abstractmethod def lacak_pengiriman(self, no_resi: str) -> str`: pass
2. **Implementasikan 3 Subclass Konkret**:
   - `JNEExpress`: Tarif dasar Rp 10.000 + (Rp 2.000 $\times$ berat) + (Rp 500 $\times$ jarak).
   - `SiCepatService`: Tarif dasar Rp 9.000 + (Rp 2.500 $\times$ berat) + (Rp 400 $\times$ jarak).
   - `PosIndonesia`: Tarif dasar Rp 8.000 + (Rp 1.800 $\times$ berat) + (Rp 600 $\times$ jarak).
3. **Instruksi Vibe Coding**:
   - Perintahkan AI membuat struktur di atas.
   - **Eksperimen Mahasiswa**: Hapus sengaja implementasi method `lacak_pengiriman` pada salah satu class konkret, lalu jalankan script. Amati error `TypeError` yang muncul dan catat penjelasannya di `PROMPT_LOG.md`.
