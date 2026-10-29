"""
Modul 04: Pewarisan (Inheritance), super(), & Method Overriding
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
class Karyawan:
    def __init__(self, id_karyawan: str, nama: str, gaji_pokok: float) -> None:
        self.id_karyawan: str = id_karyawan
        self.nama: str = nama
        self.gaji_pokok: float = gaji_pokok

    def hitung_gaji_bulanan(self) -> float:
        return self.gaji_pokok

    def cetak_slip(self) -> None:
        print(f"[{self.id_karyawan}] {self.nama} -> Total Gaji: Rp {self.hitung_gaji_bulanan():,.2f}")


class KaryawanTetap(Karyawan):
    def __init__(self, id_karyawan: str, nama: str, gaji_pokok: float, tunjangan: float) -> None:
        super().__init__(id_karyawan, nama, gaji_pokok)
        self.tunjangan: float = tunjangan

    def hitung_gaji_bulanan(self) -> float:
        return self.gaji_pokok + self.tunjangan


class KaryawanKontrak(Karyawan):
    def __init__(self, id_karyawan: str, nama: str, upah_per_jam: float, jam_kerja: int) -> None:
        super().__init__(id_karyawan, nama, gaji_pokok=0.0)
        self.upah_per_jam: float = upah_per_jam
        self.jam_kerja: int = jam_kerja

    def hitung_gaji_bulanan(self) -> float:
        return self.upah_per_jam * self.jam_kerja


if __name__ == "__main__":
    staff = [
        KaryawanTetap("EMP-01", "Budi", gaji_pokok=5_000_000, tunjangan=1_500_000),
        KaryawanKontrak("EMP-02", "Siti", upah_per_jam=50_000, jam_kerja=160),
    ]
    for s in staff:
        s.cetak_slip()\n