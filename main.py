from ekstraktor import ekstrak_pesan
from dekriptor import dekripsi_data
from pelapor import buat_laporan

def tampilkan_menu():
    print("Alat Forensik Digital iOS")
    print("=========================")
    print("1. Ekstrak dan Dekripsi Pesan")
    print("2. Buat Laporan Forensik")
    print("3. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            direktori_cadangan = input("Masukkan path ke direktori cadangan iOS: ")
            pesan = ekstrak_pesan(direktori_cadangan)
            
            kunci = b"yourkeyhere"  # Kunci AES
            iv = b"yourivhere"  # Vektor inisialisasi

            pesan_didekripsi = [dekripsi_data(p['teks'], kunci, iv) for p in pesan]

            for p in pesan_didekripsi:
                print(f"Pesan: {p}")

        elif pilihan == '2':
            direktori_cadangan = input("Masukkan path ke direktori cadangan iOS: ")
            pesan = ekstrak_pesan(direktori_cadangan)
            
            kunci = b"yourkeyhere"  # Kunci AES
            iv = b"yourivhere"  # Vektor inisialisasi

            pesan_didekripsi = [dekripsi_data(p['teks'], kunci, iv) for p in pesan]

            buat_laporan(pesan_didekripsi)
            print("Laporan forensik berhasil dibuat.")
        
        elif pilihan == '3':
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
