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
            pesanan_baru = input("Masukkan nama pesanan: ")
            antrian.enqueue(pesanan_baru)
        elif pilihan == '2':
            pesanan_dihapus = antrian.dequeue()
            if pesanan_dihapus:
                print(f"Pesanan '{pesanan_dihapus}' telah dihapus dari antrian.")
        elif pilihan == '3':
            antrian.list()
        elif pilihan == '4':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
main()
