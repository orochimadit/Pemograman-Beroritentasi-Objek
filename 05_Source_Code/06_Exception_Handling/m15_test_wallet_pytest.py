"""
Modul 15: Automated Unit Testing dengan pytest
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
Jalankan: pytest -v m15_test_wallet_pytest.py
"""
import pytest

class Wallet:
    def __init__(self, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Saldo awal tidak boleh negatif!")
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Saldo tidak mencukupi!")
        self._balance -= amount

def test_initial_balance():
    w = Wallet(50_000)
    assert w.balance == 50_000

def test_withdraw_success():
    w = Wallet(100_000)
    w.withdraw(30_000)
    assert w.balance == 70_000

def test_withdraw_insufficient():
    w = Wallet(50_000)
    with pytest.raises(ValueError):
        w.withdraw(100_000)\n