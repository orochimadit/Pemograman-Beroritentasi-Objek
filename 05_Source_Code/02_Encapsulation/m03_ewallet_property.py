"""
Modul 03: Enkapsulasi, Proteksi State & Decorator @property
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
class EWallet:
    def __init__(self, pemilik: str, saldo_awal: float = 0.0) -> None:
        self.pemilik: str = pemilik
        self._saldo: float = 0.0
        self.saldo = saldo_awal  # Melewati validasi setter!

    @property
    def saldo(self) -> float:
        """Getter untuk membaca saldo"""
        return self._saldo

    @saldo.setter
    def saldo(self, nilai: float) -> None:
        """Setter dengan filter invariant: saldo tidak boleh negatif"""
        if nilai < 0:
            raise ValueError(f"Validasi Gagal: Saldo tidak boleh negatif! (Input: {nilai})")
        self._saldo = nilai

    def tarik_tunai(self, jumlah: float) -> None:
        if jumlah <= 0:
            raise ValueError("Nominal penarikan harus lebih dari 0!")
        if jumlah > self._saldo:
            raise ValueError(f"Saldo tidak cukup! Saldo Anda: {self._saldo}, diminta: {jumlah}")
        self._saldo -= jumlah
        print(f"Penarikan Rp {jumlah:,.2f} sukses. Sisa saldo: Rp {self._saldo:,.2f}")


if __name__ == "__main__":
    dompet = EWallet("Budi", 100_000)
    print(f"Saldo Budi: Rp {dompet.saldo:,.2f}")
    dompet.tarik_tunai(40_000)\n