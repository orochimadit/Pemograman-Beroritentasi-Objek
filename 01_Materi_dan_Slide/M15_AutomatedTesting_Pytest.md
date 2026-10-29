# 📘 Modul 15: Automated Unit Testing untuk Sistem PBO (`pytest`)

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami pentingnya pengujian otomatis (*Automated Testing*) dalam siklus rekayasa perangkat lunak.
2. Menggunakan framework `pytest` untuk menguji class dan method objek.
3. Menggunakan `@pytest.fixture` untuk menyiapkan (*setup*) state objek sebelum pengujian dijalankan.
4. Memvalidasi Custom Exception menggunakan blok `pytest.raises`.
5. Menerapkan loop Vibe Coding berbasis TDD (*Test-Driven Development*).

---

## 1. Mengapa Testing Sangat Vital dalam Vibe Coding?

Saat Anda mengizinkan AI menuliskan kode, **satu-satunya cara untuk menjamin bahwa kode AI tersebut benar dan aman adalah dengan menuliskan test suite otomatis**.

```
[ Spesifikasi & Desain ] ──> [ Mahasiswa / AI Tulis Test (pytest) ]
                                            │
                                            ▼ (Jalankan: pytest -v)
                                     ❌ Tests Gagal (Red)
                                            │
                                            ▼ Mahasiswa Refactor / Prompt AI
                                     ✅ Tests Lolos (Green)
```

---

## 2. Studi Kasus Demo: Menulis Unit Test Dompet Digital

### 2.1 File Kode Objek Bisnis: `wallet.py`
```python
class InsufficientFundsError(Exception):
    pass

class Wallet:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Saldo awal tidak boleh negatif!")
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Jumlah deposit harus positif!")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Jumlah penarikan harus positif!")
        if amount > self._balance:
            raise InsufficientFundsError("Saldo tidak mencukupi!")
        self._balance -= amount
```

### 2.2 File Pengujian Otomatis: `test_wallet.py`
```python
import pytest
from wallet import Wallet, InsufficientFundsError

# 1. Menggunakan Fixture untuk inisialisasi objek pengujian
@pytest.fixture
def empty_wallet() -> Wallet:
    return Wallet("Budi", initial_balance=0.0)

@pytest.fixture
def funded_wallet() -> Wallet:
    return Wallet("Siti", initial_balance=100_000.0)


# 2. Uji Coba State Normal
def test_initial_balance(empty_wallet: Wallet):
    assert empty_wallet.balance == 0.0
    assert empty_wallet.owner == "Budi"

def test_deposit(empty_wallet: Wallet):
    empty_wallet.deposit(50_000)
    assert empty_wallet.balance == 50_000

def test_withdraw_success(funded_wallet: Wallet):
    funded_wallet.withdraw(40_000)
    assert funded_wallet.balance == 60_000


# 3. Uji Coba Penolakan Kasus Negatif (Exception Testing)
def test_withdraw_exceeding_balance(funded_wallet: Wallet):
    with pytest.raises(InsufficientFundsError):
        funded_wallet.withdraw(150_000)  # Menarik lebih dari saldo harus memicu error!

def test_deposit_negative_amount(empty_wallet: Wallet):
    with pytest.raises(ValueError):
        empty_wallet.deposit(-10_000)

def test_create_wallet_negative_initial():
    with pytest.raises(ValueError):
        Wallet("Doni", initial_balance=-500)
```

Untuk menjalankan pengujian, cukup ketik di terminal:
```bash
pytest -v test_wallet.py
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Test Suite Komprehensif Sistem Penjualan
1. Ambil kode program dari salah satu modul sebelumnya (misal: Modul 03 Sistem Nilai atau Modul 14 Diskon E-Commerce).
2. Buat file pengujian otomatis `test_aplikasi.py` dengan minimal 6 skenario pengujian:
   - Minimal 2 pengujian instansiasi normal (assert state awal).
   - Minimal 2 pengujian modifikasi state dan method bisnis.
   - Minimal 2 pengujian `pytest.raises` untuk memastikan validasi setter/enkapsulasi bekerja saat diberi input salah.
3. **Instruksi Vibe Coding**:
   - Minta AI membuatkan test case awal.
   - **Tantang AI**: Cari *edge cases* yang belum diuji oleh AI (misal: penarikan tepat seharga saldo, atau diskon yang membuat total belanja menjadi minus).
   - Pastikan seluruh test berhasil lulus (status hijau / 100% *PASSED*) dan lampirkan output terminal di `PROMPT_LOG.md`.
