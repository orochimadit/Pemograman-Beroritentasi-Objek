"""
Modul 01: Sistem Antrean Klinik (PBO Dasar vs Prosedural)
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from datetime import datetime

class Pasien:
    def __init__(self, nomor_antrean: int, nama: str, keluhan: str) -> None:
        self.nomor_antrean: int = nomor_antrean
        self.nama: str = nama
        self.keluhan: str = keluhan
        self.waktu_daftar: datetime = datetime.now()
        self.status: str = "Menunggu"

    def panggil(self) -> None:
        self.status = "Sedang Diperiksa"
        print(f"[PANGGILAN] Nomor {self.nomor_antrean}: {self.nama} menuju ruang periksa.")

    def selesai(self) -> None:
        self.status = "Selesai"
        print(f"[SELESAI] Pasien {self.nama} telah menyelesaikan pemeriksaan.")


class AntreanKlinik:
    def __init__(self, nama_poli: str) -> None:
        self.nama_poli: str = nama_poli
        self.daftar_pasien: list[Pasien] = []

    def daftar_pasien_baru(self, nama: str, keluhan: str) -> Pasien:
        nomor_baru = len(self.daftar_pasien) + 1
        pasien = Pasien(nomor_baru, nama, keluhan)
        self.daftar_pasien.append(pasien)
        print(f"Pendaftaran sukses: {nama} (No. {nomor_baru}) di {self.nama_poli}")
        return pasien


if __name__ == "__main__":
    poli = AntreanKlinik("Poli Umum")
    p1 = poli.daftar_pasien_baru("Budi Santoso", "Demam tinggi")
    p2 = poli.daftar_pasien_baru("Siti Rahma", "Pemeriksaan mata")
    p1.panggil()
    p1.selesai()\n