"""
Modul 06: Penanganan Error Objek (Custom Exceptions)
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
class ATMError(Exception):
    pass

class SaldoTidakCukupError(ATMError):
    def __init__(self, saldo_aktif: float, jumlah_tarik: float) -> None:
        self.saldo_aktif = saldo_aktif
        self.jumlah_tarik = jumlah_tarik
        self.selisih = jumlah_tarik - saldo_aktif
        super().__init__(f"Saldo kurang Rp {self.selisih:,.2f}! Saldo: Rp {saldo_aktif:,.2f}")

class RekeningBank:
    def __init__(self, no_rek: str, saldo_awal: float) -> None:
        self.no_rek = no_rek
        self.saldo = saldo_awal

    def tarik(self, nominal: float) -> None:
        if nominal > self.saldo:
            raise SaldoTidakCukupError(self.saldo, nominal)
        self.saldo -= nominal
        print(f"Penarikan Rp {nominal:,.2f} sukses. Sisa saldo: Rp {self.saldo:,.2f}")

if __name__ == "__main__":
    rek = RekeningBank("123-456", 500_000)
    try:
        rek.tarik(750_000)
    except SaldoTidakCukupError as e:
        print(f"[DITOLAK]: {e}")
        print(f"Kekurangan dana: Rp {e.selisih:,.2f}")\n