"""
Modul 11: Komposisi vs Pewarisan (Favor Composition Over Inheritance)
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from abc import ABC, abstractmethod

class SenjataBehavior(ABC):
    @abstractmethod
    def gunakan(self) -> str:
        pass

class Pedang(SenjataBehavior):
    def gunakan(self) -> str:
        return "menebaskan pedang tajam!"

class TongkatSihir(SenjataBehavior):
    def gunakan(self) -> str:
        return "menembakkan bola api sihir!"

class Hero:
    def __init__(self, nama: str, senjata: SenjataBehavior) -> None:
        self.nama = nama
        self.senjata = senjata

    def serang(self) -> None:
        print(f"[{self.nama}] {self.senjata.gunakan()}")

    def ganti_senjata(self, senjata_baru: SenjataBehavior) -> None:
        self.senjata = senjata_baru
        print(f"*** {self.nama} mengganti senjatanya! ***")

if __name__ == "__main__":
    hero = Hero("Arthur", Pedang())
    hero.serang()
    hero.ganti_senjata(TongkatSihir())
    hero.serang()\n