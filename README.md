# iOS Digital Forensic Tool

Alat forensik digital untuk perangkat iOS yang memungkinkan ekstraksi, dekripsi, dan analisis pesan yang terhapus. Aplikasi ini menggunakan Python dan dilengkapi dengan fitur-fitur canggih seperti organisasi data yang rapi, antarmuka pengguna berbasis CLI yang interaktif, dan visualisasi data dalam bentuk grafik.

## Fitur

- **Ekstraksi Pesan**: Menarik pesan teks yang tersimpan di perangkat iOS dari backup.
- **Dekripsi Data**: Mendekripsi pesan yang terenkripsi menggunakan kunci AES.
- **Organisasi Data**: Mengorganisir pesan yang diekstraksi dengan metadata tambahan seperti tanggal, waktu, pengirim, dan penerima.
- **Antarmuka Pengguna Berbasis CLI**: Antarmuka pengguna berbasis command-line yang interaktif untuk navigasi data.
- **Visualisasi Data**: Menyediakan grafik linimasa untuk visualisasi data dalam laporan PDF.
- **Laporan Forensik PDF**: Membuat laporan forensik dalam format PDF yang mudah dibaca dan dipahami.

## Struktur Proyek
```
ios-digital-forensic-tool/
├── main.py
├── ekstraktor.py
├── dekriptor.py
├── pelapor.py
└── requirements.txt

```
## Instalasi

1. Clone repository ini:
```
git clone https://github.com/username/ios-digital-forensic-tool.git

```
2. Navigasi ke direktori proyek:
```
cd ios-digital-forensic-tool
```
3. Install dependensi:
```
pip install -r requirements.txt
```
## Penggunaan
1. Jalankan `main.py`:
```
python main.py
```
2. Ikuti petunjuk pada antarmuka CLI untuk mengekstrak dan menganalisis pesan atau membuat laporan forensik.

## Contoh

Setelah mengikuti petunjuk penggunaan, alat ini akan mengekstrak pesan dari backup iOS, mendekripsi data yang diperlukan, dan menghasilkan laporan forensik dalam format PDF dengan visualisasi data yang rapi.

## Kontribusi

Kami menyambut kontribusi dari pengembang lain. Silakan fork repository ini dan ajukan pull request dengan penjelasan tentang perubahan yang Anda buat.