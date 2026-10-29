"""
Modul 14: Behavioral Patterns: Strategy & Observer
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from abc import ABC, abstractmethod

# Strategy Pattern
class DiskonStrategy(ABC):
    @abstractmethod
    def hitung(self, total: float) -> float:
        pass

class DiskonVIP(DiskonStrategy):
    def hitung(self, total: float) -> float:
        return total * 0.15

class DiskonReguler(DiskonStrategy):
    def hitung(self, total: float) -> float:
        return 0.0

class Keranjang:
    def __init__(self, strategi: DiskonStrategy) -> None:
        self.strategi = strategi

    def checkout(self, subtotal: float) -> float:
        potongan = self.strategi.hitung(subtotal)
        return subtotal - potongan

if __name__ == "__main__":
    cart = Keranjang(DiskonVIP())
    print("Total Bayar VIP:", cart.checkout(200_000))\n