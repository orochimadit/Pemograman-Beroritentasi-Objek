"""
Modul 13: Creational & Structural Patterns: Factory & Facade
Mata Kuliah: Pemrograman Berorientasi Objek
Pemateri: Aditya Pratama
"""
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, data: str) -> None:
        pass

class PDFExporter(Exporter):
    def export(self, data: str) -> None:
        print(f"[PDF]: Mengekspor '{data}' ke dokumen PDF.")

class ExcelExporter(Exporter):
    def export(self, data: str) -> None:
        print(f"[EXCEL]: Mengekspor '{data}' ke tabel Excel.")

class ExporterFactory:
    @staticmethod
    def create_exporter(format_type: str) -> Exporter:
        if format_type.lower() == "pdf":
            return PDFExporter()
        elif format_type.lower() == "excel":
            return ExcelExporter()
        raise ValueError(f"Format {format_type} tidak didukung!")

if __name__ == "__main__":
    exp = ExporterFactory.create_exporter("pdf")
    exp.export("Laporan Penjualan")\n