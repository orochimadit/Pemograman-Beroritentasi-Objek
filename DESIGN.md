# Desain & Identitas Visual: Pemrograman Berorientasi Objek (PBO)

Dokumen ini memuat panduan identitas visual, token desain, dan aturan anti-slop untuk materi perkuliahan Pemrograman Berorientasi Objek (PBO) berbasis Python modern dan Vibe Coding di bawah pengampu **Aditya Pratama**.

---

## 1. Dials (Karakter Antarmuka & Materi)

- **ENERGY: 1** (Fokus pada keterbacaan kode, diagram arsitektur objek, dan ketepatan terminologi teknis).
- **RHYTHM: 2** (Hierarki tajam: capaian kompetensi, abstraksi masalah, implementasi kode PEP 8, audit kesalahan AI, dan lembar verifikasi).
- **MOTION: 1** (Transisi fungsional murni antar slide, bebas efek kosmetik yang memperlambat fokus belajar).

---

## 2. Palet Token Warna (Academic Deep Navy & Cyan)

Palet dirancang berbasis tema gelap kontras tinggi untuk kenyamanan proyeksi kelas dan keterbacaan kode terminal:

- **Latar Halaman (`--bg-page`)**: `#0a0f1d` (Deep Navy)
- **Kontainer Kartu (`--card-bg`)**: `#131b2e` (Slate Dark)
- **Batas Kontainer (`--card-border`)**: `#1f2d4a` (Slate Border)
- **Aksen Primer PBO (`--primary`)**: `#38bdf8` (Cyan 400)
- **Aksen Sekunder / Hover (`--primary-hover`)**: `#0284c7` (Cyan 600)
- **Aksen In-Lab / Lulus (`--badge-inlab`)**: `#10b981` (Emerald 500)
- **Aksen Take-Home / Mandiri (`--badge-takehome`)**: `#818cf8` (Indigo 400)
- **Teks Utama (`--text-main`)**: `#f8fafc` (Slate 50, kontras > 14:1)
- **Teks Keterangan (`--text-muted`)**: `#94a3b8` (Slate 400, kontras > 4.5:1)
- **Latar Blok Kode (`--code-bg`)**: `#060913` (Terminal Black)

---

## 3. Tipografi & Tata Huruf

- **Teks Antarmuka & Heading**: System Sans-Serif (`system-ui`, `-apple-system`, `"Segoe UI"`, `Roboto`, `sans-serif`)
  - Bersih, terstruktur, tanpa ornamen dekoratif.
- **Kode Program & Notasi UML**: Monospace murni (`ui-monospace`, `"SF Mono"`, `"Consolas"`, `monospace`)
  - Dipakai wajib pada nama class, method, type hints, dan perintah terminal.

---

## 4. Standar Hallmark Anti-Slop (The Floor)

Seluruh slide presentasi dan materi web mematuhi aturan berikut:
1. **Bebas Polusi Em Dash**: Gunakan tanda titik dua (`:`), tanda hubung biasa (`-`), koma (`,`), atau kurung `()`.
2. **Bebas Polusi Emoji**: Hapus seluruh ikon emoji generik di heading; gantikan dengan label badge bertoken teks yang tegas.
3. **Bebas Kalimat AI Basa-Basi**: Hindari klise *"Di era modern yang serba cepat ini"* atau *"Sebagai programmer handal"*. Langsung masuk ke esensi teknis, alasan arsitektural, dan instruksi eksekusi.
4. **CSS Stamp & Token Terpusat**: Baris pertama CSS slide selalu memuat stamp Hallmark, diikuti deklarasi variabel di `:root`.
5. **Transisi Terbatas & Spesifik**: Dilarang menggunakan `transition: all`. Setiap animasi dibatasi pada `opacity` atau `transform` dengan durasi singkat (0.15s - 0.2s).
6. **Kepadatan Informasi Terukur**: Maksimal ~80 kata per slide agar materi di layar proyektor dapat dipahami mahasiswa dalam 10 detik.
7. **Identitas Pengampu**: Cukup ditulis **Aditya Pratama** secara lugas tanpa tambahan gelar.
