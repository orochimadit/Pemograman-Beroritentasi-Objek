"""
Modul 07: Abstraksi, Abstract Base Classes (ABCs), & Interface
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def bayar(self, nominal: float) -> bool:
        pass

    @abstractmethod
    def refund(self, id_transaksi: str) -> bool:
        pass

class MidtransPayment(PaymentProcessor):
    def bayar(self, nominal: float) -> bool:
        print(f"[MIDTRANS]: Pembayaran QRIS Rp {nominal:,.2f} sukses.")
        return True

    def refund(self, id_transaksi: str) -> bool:
        print(f"[MIDTRANS]: Refund transaksi {id_transaksi} diproses.")
        return True

def proses_checkout(gateway: PaymentProcessor, total: float) -> None:
    gateway.bayar(total)

if __name__ == "__main__":
    proses_checkout(MidtransPayment(), 250_000)\n