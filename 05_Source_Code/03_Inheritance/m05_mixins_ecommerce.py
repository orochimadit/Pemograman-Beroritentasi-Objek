"""
Modul 05: Multiple Inheritance & Mixin Pattern
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
import json
from datetime import datetime

class TimestampMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class JSONExportMixin:
    def to_json(self) -> str:
        data = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return json.dumps(data, indent=2)

class Produk:
    def __init__(self, sku: str, nama: str, harga: float) -> None:
        self.sku = sku
        self.nama = nama
        self.harga = harga

class ProdukECommerce(TimestampMixin, JSONExportMixin, Produk):
    def __init__(self, sku: str, nama: str, harga: float, kategori: str) -> None:
        self.kategori = kategori
        super().__init__(sku=sku, nama=nama, harga=harga)

if __name__ == "__main__":
    p = ProdukECommerce("SKU-001", "Laptop Gaming", 15_000_000, "Elektronik")
    print(p.to_json())
    print("\nUrutan MRO:", [c.__name__ for c in ProdukECommerce.__mro__])\n