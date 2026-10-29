# 📘 Modul 11: Komposisi vs Pewarisan (*Composition Over Inheritance*)

## 🎯 Capaian Pembelajaran Pertemuan
Setelah menyelesaikan pertemuan ini, mahasiswa diharapkan mampu:
1. Memahami prinsip desain fundamental: *"Favor Composition over Inheritance"*.
2. Mengidentifikasi kelemahan hierarki pewarisan bertingkat (*Fragile Base Class problem*).
3. Merancang sistem dengan relasi *Has-A* (komposisi) agar komponen lebih fleksibel dan mudah diganti saat runtime.
4. Menggunakan objek yang dapat dipanggil (*callable objects*) dengan dunder method `__call__`.

---

## 1. Mengapa Terlalu Banyak Inheritance Berbahaya?

Bayangkan Anda merancang game RPG. Jika menggunakan inheritance murni:
- `Karakter` $\rightarrow$ `Ksatria`
- Ingin ksatria yang bisa sihir? Buat `KsatriaSihir`.
- Ingin ksatria sihir terbang? Buat `KsatriaSihirTerbang`.

```
                    [ Karakter ]
                    /          \
              [ Ksatria ]     [ Penyihir ]
                 /
      [ KsatriaSihir ]  <-- Ledakan Subclass (Subclass Explosion)!
```

Sistem menjadi kaku (*rigid*). Jika class `Karakter` diubah, seluruh turunan di bawahnya berisiko rusak.

---

## 2. Solusi: Komposisi (*Composition*)

Alih-alih mendefinisikan *apa jenis objek tersebut* (*is-a*), kita mendefinisikan *apa yang dimiliki objek tersebut* (*has-a*).

```
+-------------------------------------------------------+
|                        HERO                           |
|                                                       |
|  - nama: str                                          |
|  - senjata: SenjataComponent        (has-a)           |
|  - pergerakan: PergerakanComponent  (has-a)           |
|                                                       |
|  + serang() -> self.senjata.gunakan()                 |
|  + bergerak() -> self.pergerakan.pindah()             |
+-------------------------------------------------------+
```

---

## 3. Studi Kasus Demo: Game RPG dengan Komponen Modular

```python
from abc import ABC, abstractmethod

# Komponen Perilaku Senjata
class SenjataBehavior(ABC):
    @abstractmethod
    def gunakan(self) -> str:
        pass

class PedangBesi(SenjataBehavior):
    def gunakan(self) -> str:
        return "menebaskan Pedang Besi! (Damage: 45)"

class TongkatSihir(SenjataBehavior):
    def gunakan(self) -> str:
        return "menembakkan Bola Api Sihir! (Damage: 80)"


# Komponen Perilaku Gerak
class PergerakanBehavior(ABC):
    @abstractmethod
    def bergerak(self) -> str:
        pass

class BerjalanKaki(PergerakanBehavior):
    def bergerak(self) -> str:
        return "berjalan perlahan di tanah."

class TerbangSayap(PergerakanBehavior):
    def bergerak(self) -> str:
        return "terbang cepat melintasi langit!"


# Class Utama (Hanya menggabungkan komponen via Komposisi)
class Hero:
    def __init__(
        self,
        nama: str,
        senjata: SenjataBehavior,
        pergerakan: PergerakanBehavior
    ) -> None:
        self.nama = nama
        self.senjata = senjata
        self.pergerakan = pergerakan

    def beraksi(self) -> None:
        print(f"[{self.nama}] {self.pergerakan.bergerak()}")
        print(f"[{self.nama}] {self.senjata.gunakan()}")

    def ganti_senjata(self, senjata_baru: SenjataBehavior) -> None:
        print(f"*** {self.nama} mengganti senjatanya! ***")
        self.senjata = senjata_baru


# Demo Fleksibilitas Komposisi di Runtime
if __name__ == "__main__":
    artoria = Hero(
        nama="Artoria Pendragon",
        senjata=PedangBesi(),
        pergerakan=BerjalanKaki()
    )
    artoria.beraksi()

    # Mengubah kemampuan di tengah jalan tanpa membuat subclass baru!
    artoria.ganti_senjata(TongkatSihir())
    artoria.pergerakan = TerbangSayap()
    artoria.beraksi()
```

---

## 4. Lembar Tugas Praktikum Mahasiswa

### 📝 Tugas: Sistem Perakit Komputer Custom (PC Builder)
1. **Rancang Komponen**:
   - `Processor`: `merk: str`, `kecepatan_ghz: float`, `watt: int`.
   - `RAM`: `kapasitas_gb: int`, `tipe_ddr: str`, `watt: int`.
   - `GPU`: `chipset: str`, `vram_gb: int`, `watt: int`.
   - `PowerSupply`: `kapasitas_watt: int`.
2. **Rancang Class `Komputer`**:
   - Menerima komponen di atas melalui constructor (komposisi).
   - Method `hitung_kebutuhan_daya() -> int` (menjumlahkan watt CPU + RAM + GPU).
   - Method `cek_kelayakan_daya() -> bool` (memastikan kapasitas PSU > kebutuhan daya).
3. **Instruksi Vibe Coding**:
   - Minta AI sengaja merancang sistem ini dengan cara *inheritance* (`KomputerGaming` turunan dari `GPU`).
   - Tuliskan ulasan kritis di `PROMPT_LOG.md` mengapa inheritance buruk untuk kasus ini.
   - Perintahkan AI untuk me-*refactor* seluruh rancangan menjadi model komposisi murni!
