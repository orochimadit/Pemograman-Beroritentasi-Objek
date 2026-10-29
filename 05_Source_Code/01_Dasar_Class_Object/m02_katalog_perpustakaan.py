"""
Modul 02: Objek, Class, State, Behavior & Type Hints
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
class Buku:
    # Class Attribute untuk melacak total stok semua buku di perpustakaan
    total_inventaris_buku: int = 0

    def __init__(self, isbn: str, judul: str, penulis: str, stok: int = 1) -> None:
        # Instance Attributes
        self.isbn: str = isbn
        self.judul: str = judul
        self.penulis: str = penulis
        self.stok: int = stok
        Buku.total_inventaris_buku += stok

    def pinjam(self) -> bool:
        if self.stok > 0:
            self.stok -= 1
            print(f"Buku '{self.judul}' dipinjam. Sisa stok: {self.stok}")
            return True
        print(f"Stok buku '{self.judul}' habis!")
        return False

    def kembalikan(self) -> None:
        self.stok += 1
        print(f"Buku '{self.judul}' dikembalikan. Stok: {self.stok}")


class Anggota:
    def __init__(self, nim: str, nama: str) -> None:
        self.nim: str = nim
        self.nama: str = nama
        self.buku_pinjaman: list[Buku] = []

    def pinjam_buku(self, buku: Buku) -> None:
        if buku.pinjam():
            self.buku_pinjaman.append(buku)


if __name__ == "__main__":
    b1 = Buku("978-01", "Python OOP 4th Edition", "Dusty Phillips", stok=2)
    mhs = Anggota("12345", "Budi")
    mhs.pinjam_buku(b1)\n