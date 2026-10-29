"""
Modul 10: Struktur Data Modern & Python Dataclasses
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Seat:
    baris: str
    nomor: int
    kategori: str

@dataclass
class TiketKonser:
    id_tiket: str
    seat: Seat
    harga: float
    fasilitas: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.seat.kategori == "VIP" and self.harga < 1_000_000:
            raise ValueError("Harga tiket kategori VIP minimal Rp 1.000.000!")

if __name__ == "__main__":
    s = Seat("A", 12, "VIP")
    t = TiketKonser("T-001", s, 1_500_000, fasilitas=["Snack", "Lounge"])
    print(t)\n