# 📘 Modul 09: Magic / Dunder Methods & Operator Overloading

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami konsep metode spesial / *dunder (double underscore)* di Python.
2. Membedakan fungsi representasi objek: `__str__` (untuk pengguna) vs `__repr__` (untuk developer).
3. Menerapkan *Operator Overloading* aritmatika (`+`, `-`, `*`) dan perbandingan (`==`, `<`, `>`).
4. Mengimplementasikan protokol koleksi: `__len__`, `__getitem__`, dan `__contains__`.

---

## 1. Apa itu Magic / Dunder Methods?

Dunder methods adalah metode khusus yang diawali dan diakhiri dengan dua garis bawah (`__`). Metode ini memungkinkan objek buatan kita berperilaku seperti tipe data bawaan Python (seperti `int`, `str`, atau `list`).

| Operator / Fungsi Bawaan | Dunder Method yang Dipanggil di Balik Layar |
| :--- | :--- |
| `print(obj)` / `str(obj)` | `obj.__str__()` |
| `obj` (di REPL/Debugger) | `obj.__repr__()` |
| `obj1 + obj2` | `obj1.__add__(obj2)` |
| `obj1 == obj2` | `obj1.__eq__(obj2)` |
| `obj1 < obj2` | `obj1.__lt__(obj2)` |
| `len(obj)` | `obj.__len__()` |
| `obj[0]` | `obj.__getitem__(0)` |
| `"item" in obj` | `obj.__contains__("item")` |

---

## 2. Studi Kasus Demo: Tipe Data Uang Multi-Valuta (`Money`)

```python
from functools import total_ordering

@total_ordering  # Otomatis melengkapi operator <=, >, >= jika __eq__ dan __lt__ didefinisikan
class Money:
    def __init__(self, amount: float, currency: str = "IDR") -> None:
        self.amount = round(amount, 2)
        self.currency = currency.upper()

    def __repr__(self) -> str:
        """Untuk developer (reproducible expression)"""
        return f"Money(amount={self.amount}, currency='{self.currency}')"

    def __str__(self) -> str:
        """Untuk tampilan antarmuka pengguna"""
        if self.currency == "IDR":
            return f"Rp {self.amount:,.2f}"
        return f"{self.currency} {self.amount:,.2f}"

    def __add__(self, other: "Money") -> "Money":
        """Operator Overloading untuk tanda +"""
        if not isinstance(other, Money):
            raise TypeError("Hanya bisa menjumlahkan sesama objek Money!")
        if self.currency != other.currency:
            raise ValueError(f"Tidak bisa menjumlahkan valuta berbeda: {self.currency} dan {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other: object) -> bool:
        """Operator Overloading untuk tanda =="""
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other: "Money") -> bool:
        """Operator Overloading untuk tanda <"""
        if not isinstance(other, Money):
            raise TypeError("Hanya bisa membandingkan sesama objek Money!")
        if self.currency != other.currency:
            raise ValueError("Tidak bisa membandingkan valuta berbeda!")
        return self.amount < other.amount


# Uji Coba Operator Overloading
if __name__ == "__main__":
    dompet_1 = Money(50_000, "IDR")
    dompet_2 = Money(75_000, "IDR")

    # Menggunakan operator + langsung antar objek!
    total = dompet_1 + dompet_2
    print(f"Total: {total}")            # Memanggil __str__: Rp 125,000.00
    print(f"Debug: {repr(total)}")       # Memanggil __repr__: Money(amount=125000.0, currency='IDR')
    print(f"Apakah dompet 1 < dompet 2? {dompet_1 < dompet_2}")  # Output: True
```

---

## 3. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Keranjang Belanja Pintar (`ShoppingCart`)
1. **Buat Class `Item`**:
   - Atribut: `nama: str`, `harga: float`.
   - Implementasikan `__repr__` dan `__eq__`.
2. **Buat Class `ShoppingCart`**:
   - Atribut: `items: list[Item]`.
   - Implementasikan Dunder Methods:
     - `__len__`: Mengembalikan total jumlah barang saat dipanggil `len(cart)`.
     - `__getitem__`: Mengambil item berdasarkan indeks `cart[0]`.
     - `__contains__`: Mengecek keberadaan barang via `if "Kopi" in cart:`.
     - `__add__`: Menggabungkan dua keranjang belanja (`cart3 = cart1 + cart2`).
3. **Instruksi Vibe Coding**:
   - Minta AI membuat class tersebut.
   - Uji kode AI dengan ekspresi `cart1 + cart2`. Pastikan AI mengembalikan objek `ShoppingCart` baru dan tidak mengubah isi objek aslinya (*immutable addition*).
   - Catat proses testing di `PROMPT_LOG.md`.
