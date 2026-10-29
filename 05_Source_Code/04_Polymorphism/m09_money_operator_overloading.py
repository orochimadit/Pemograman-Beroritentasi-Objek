"""
Modul 09: Magic / Dunder Methods & Operator Overloading
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount: float, currency: str = "IDR") -> None:
        self.amount = round(amount, 2)
        self.currency = currency.upper()

    def __repr__(self) -> str:
        return f"Money(amount={self.amount}, currency='{self.currency}')"

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:,.2f}"

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money) or self.currency != other.currency:
            raise ValueError("Hanya bisa menjumlahkan valuta yang sama!")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return (self.amount, self.currency) == (other.amount, other.currency)

    def __lt__(self, other: "Money") -> bool:
        if not isinstance(other, Money) or self.currency != other.currency:
            raise ValueError("Tidak dapat membandingkan valuta berbeda!")
        return self.amount < other.amount

if __name__ == "__main__":
    m1 = Money(50_000, "IDR")
    m2 = Money(75_000, "IDR")
    print("Total:", m1 + m2)
    print("Apakah m1 < m2?", m1 < m2)\n