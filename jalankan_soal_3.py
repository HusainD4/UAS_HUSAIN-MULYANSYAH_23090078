from soal_3 import Queue

me = "HUSAIN MULYANSYAH"
no = "23090078"

print(f"NAMA\t: {me},\nNIM\t:{no}\n")

def main():
    antrian = Queue()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            nama_pemesan = input("Masukkan nama pemesan: ")
            menu_pesanan = input("Masukkan menu yang dipesan: ")
            antrian.enqueue(nama_pemesan, menu_pesanan)
        elif pilihan == '2':
            pesanan_dihapus = antrian.dequeue()
            if pesanan_dihapus != "Antrian kosong":
                print(f"Pesanan '{pesanan_dihapus['menu']}' untuk '{pesanan_dihapus['nama']}' telah dihapus dari antrian.")
            else:
                print(pesanan_dihapus)
        elif pilihan == '3':
            print("========== DATA ANTRIAN ==========")
            antrian.data_pelanggan()
        elif pilihan == '4':
            print("\nProgram selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

main()
