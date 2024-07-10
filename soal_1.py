me = "HUSAIN MULYANSYAH"
no = "23090078"

print(f"NAMA\t: {me},\nNIM\t:{no}\n")

def soal1():
    data_mahasiswa = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        
        data_mahasiswa.append({'NIM': nim, 'Nama': nama})
        
        tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
        if tambah_lagi != 'ya':
            break


    print("\nData Mahasiswa:")
    for index, mahasiswa in enumerate(data_mahasiswa, start=1):
        print(f"{index}. {mahasiswa['Nama']} ({mahasiswa['NIM']})")
soal1()