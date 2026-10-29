"""
Modul 08: Core Auction Engine (Studi Kasus Mandiri UTS)
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from abc import ABC, abstractmethod

class LelangError(Exception):
    pass

class PenawaranTerlaluRendahError(LelangError):
    pass

class BarangLelang:
    def __init__(self, id_barang: str, nama: str, harga_awal: float) -> None:
        self.id_barang = id_barang
        self.nama = nama
        self.harga_awal = harga_awal
        self._penawaran_tertinggi = harga_awal
        self._pemenang_sementara: str | None = None

    @property
    def penawaran_tertinggi(self) -> float:
        return self._penawaran_tertinggi

    def ajukan_tawaran(self, nama_penawar: str, nominal: float) -> None:
        if nominal <= self._penawaran_tertinggi:
            raise PenawaranTerlaluRendahError(f"Tawaran Rp {nominal:,.2f} harus > Rp {self._penawaran_tertinggi:,.2f}")
        self._penawaran_tertinggi = nominal
        self._pemenang_sementara = nama_penawar
        print(f"[BID BARU]: {nama_penawar} memimpin dengan Rp {nominal:,.2f}")

if __name__ == "__main__":
    item = BarangLelang("A01", "Lukisan Antik", 1_000_000)
    item.ajukan_tawaran("Budi", 1_200_000)
    item.ajukan_tawaran("Siti", 1_500_000)\n