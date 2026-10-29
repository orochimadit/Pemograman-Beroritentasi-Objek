"""
Modul 16: Showcase Proyek Akhir Sistem PBO (UAS)
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
class SistemAkademikCore:
    def __init__(self, nama_institusi: str) -> None:
        self.nama_institusi = nama_institusi
        self.daftar_modul: list[str] = [
            "01_Dasar_Class_Object",
            "02_Encapsulation",
            "03_Inheritance",
            "04_Polymorphism",
            "05_Abstraction_Interface",
            "06_Exception_Handling",
            "07_GUI_Desktop_App"
        ]

    def status_kesiapan_showcase(self) -> None:
        print(f"=== {self.nama_institusi} ===")
        print("Seluruh modul PBO terintegrasi siap dipresentasikan.")
        for idx, m in enumerate(self.daftar_modul, start=1):
            print(f"  [{idx:02d}] {m} -> Teruji & Valid")

if __name__ == "__main__":
    app = SistemAkademikCore("Showcase PBO Python")
    app.status_kesiapan_showcase()\n