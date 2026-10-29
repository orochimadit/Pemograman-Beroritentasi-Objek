# 📘 Modul 14: Behavioral Design Patterns (Strategy & Observer)

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami pola desain perilaku (*Behavioral Patterns*): **Strategy Pattern** dan **Observer Pattern**.
2. Menerapkan **Strategy Pattern** untuk mengganti algoritma atau aturan bisnis saat *runtime* tanpa mengubah class konteks.
3. Menerapkan **Observer Pattern** (Publish-Subscribe) untuk membangun arsitektur komunikasi objek berbasis event (*event-driven*).
4. Menghubungkan banyak observer secara *loose coupling*.

---

## 1. Strategy Pattern (Keluarga Algoritma yang Dapat Ditukar)

Alih-alih menumpuk puluhan `if-elif` di dalam class kalkulasi transaksi, kita pisahkan setiap skema algoritma ke dalam class strategi masing-masing.

```
       +-------------------------------+
       |             CART              |
       |  - strategi: DiskonStrategy   | ─────────┐
       |  + set_strategi(strategi)     |          │
       |  + checkout()                 |          │
       +-------------------------------+          │
                                                  ▼ mendelegasikan
                                      << Abstract Strategy >>
                                           DiskonStrategy
                                                  ▲
                           ┌──────────────────────┴──────────────────────┐
                           │                                             │
               +-----------------------+                     +-----------------------+
               |      DiskonMember     |                     |    DiskonFlashSale    |
               +-----------------------+                     +-----------------------+
```

---

## 2. Observer Pattern (Pola Publish-Subscribe)

Subject (Penerbit) memberitahu secara otomatis semua Observer (Pelanggan) yang terdaftar ketika terjadi perubahan data penting.

```
                  +--------------------------------+
                  |      SUBJECT (StockTicker)     |
                  |  - observers: list[Observer]   |
                  |  + attach(observer)            |
                  |  + notify_all()                |
                  +--------------------------------+
                                  │
          ┌───────────────────────┼───────────────────────┐
          ▼                       ▼                       ▼
+-------------------+   +-------------------+   +-------------------+
|  EmailAlertObserver|  | TelegramBotObserver|  | FileAuditObserver |
+-------------------+   +-------------------+   +-------------------+
```

---

## 3. Studi Kasus Demo: Kalkulator Diskon Fleksibel (Strategy)

```python
from abc import ABC, abstractmethod

# 1. Interface Strategi Diskon
class DiskonStrategy(ABC):
    @abstractmethod
    def hitung_diskon(self, total_belanja: float) -> float:
        pass

# 2. Implementasi Strategi Konkret
class DiskonTanpaSyarat(DiskonStrategy):
    def hitung_diskon(self, total_belanja: float) -> float:
        return 0.0

class DiskonMemberVIP(DiskonStrategy):
    def hitung_diskon(self, total_belanja: float) -> float:
        return total_belanja * 0.15  # Diskon tetap 15%

class DiskonFlashSale(DiskonStrategy):
    def hitung_diskon(self, total_belanja: float) -> float:
        if total_belanja >= 200_000:
            return 50_000.0  # Potongan flat Rp 50.000
        return 0.0


# 3. Class Konteks yang Memanfaatkan Strategi
class KeranjangBelanja:
    def __init__(self, strategi_diskon: DiskonStrategy = DiskonTanpaSyarat()) -> None:
        self.daftar_harga: list[float] = []
        self.strategi_diskon: DiskonStrategy = strategi_diskon

    def tambah_produk(self, harga: float) -> None:
        self.daftar_harga.append(harga)

    def set_strategi_diskon(self, strategi_baru: DiskonStrategy) -> None:
        """Mengganti skema diskon saat runtime!"""
        self.strategi_diskon = strategi_baru

    def hitung_total_akhir(self) -> float:
        subtotal = sum(self.daftar_harga)
        potongan = self.strategi_diskon.hitung_diskon(subtotal)
        total_bayar = max(0.0, subtotal - potongan)
        print(f"Subtotal: Rp {subtotal:,.2f} | Potongan: Rp {potongan:,.2f} | Total: Rp {total_bayar:,.2f}")
        return total_bayar


# Uji Coba Fleksibilitas Strategi
if __name__ == "__main__":
    cart = KeranjangBelanja()
    cart.tambah_produk(150_000)
    cart.tambah_produk(100_000)

    print("--- 1. Pembeli Reguler ---")
    cart.hitung_total_akhir()

    print("\n--- 2. Pembeli Login Sebagai VIP ---")
    cart.set_strategi_diskon(DiskonMemberVIP())
    cart.hitung_total_akhir()

    print("\n--- 3. Menggunakan Voucher Flash Sale ---")
    cart.set_strategi_diskon(DiskonFlashSale())
    cart.hitung_total_akhir()
```

---

## 4. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Pemantau Harga Saham / Kripto (Observer Pattern)
1. **Rancang Interface `Observer(ABC)`**:
   - `@abstractmethod def update(self, simbol: str, harga_baru: float) -> None`: pass
2. **Rancang Subject `CryptoPriceSubject`**:
   - Atribut: `_observers: list[Observer]`, `_daftar_harga: dict[str, float]`.
   - Method: `attach(obs: Observer)`, `detach(obs: Observer)`, `ubah_harga(simbol: str, harga: float)`.
3. **Buat 2 Concrete Observer**:
   - `TelegramAlertObserver`: Mencetak `"[TELEGRAM]: Simbol {simbol} sekarang menyentuh Rp {harga}"`.
   - `PriceHistoryLoggerObserver`: Menuliskan perubahan harga ke dalam list riwayat log internal.
4. **Instruksi Vibe Coding**:
   - Arahkan AI untuk mengimplementasikan pola Observer ini.
   - Uji penambahan observer baru tanpa merusak kode `CryptoPriceSubject`.
   - Catat bukti pengujian di `PROMPT_LOG.md`.
