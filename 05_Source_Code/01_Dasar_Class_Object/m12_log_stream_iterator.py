"""
Modul 12: Iterator Protocol & Generator Objects
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from typing import Iterator

class ProductCatalogStream:
    def __init__(self, total_produk: int = 100, batch_size: int = 10) -> None:
        self.total = total_produk
        self.batch_size = batch_size
        self.current = 0

    def __iter__(self) -> "ProductCatalogStream":
        return self

    def __next__(self) -> list[str]:
        if self.current >= self.total:
            raise StopIteration
        batch = [f"Produk-{i+1}" for i in range(self.current, min(self.current + self.batch_size, self.total))]
        self.current += self.batch_size
        return batch

if __name__ == "__main__":
    catalog = ProductCatalogStream(total_produk=35, batch_size=10)
    for batch in catalog:
        print("Batch Produk:", batch)\n