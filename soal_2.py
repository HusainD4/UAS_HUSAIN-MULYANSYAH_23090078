me = "HUSAIN MULYANSYAH"
no = "23090078"

print(f"NAMA\t: {me},\nNIM\t:{no}\n")


nama = ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"]
matkul = ["Algoritma dan Struktur Data 2", "Matematika Numerik"]
nilai_algoritma = [90, 50, 65]
nilai_matematika_numerik = [80, 60, 70]
nilai_matkul = [nilai_algoritma, nilai_matematika_numerik]

def rata_rata_matakuliah(matkul, nilai_matkul):
    rata_rata = {}
    for i in range(len(matkul)):
        rata_rata[matkul[i]] = sum(nilai_matkul[i]) / len(nilai_matkul[i])
    return rata_rata

def rata_rata_mahasiswa(nama, nilai_matkul):
    rata_rata = {}
    for i in range(len(nama)):
        total_nilai = 0
        jumlah_matkul = len(nilai_matkul)
        for nilai in nilai_matkul:
            total_nilai += nilai[i]
        rata_rata[nama[i]] = total_nilai / jumlah_matkul
    return rata_rata


rata_rata_matkul = rata_rata_matakuliah(matkul, nilai_matkul)
print("==============================================")
print("1. Rata-rata nilai untuk setiap mata kuliah:")
print("==============================================")
for matakuliah, rata2 in rata_rata_matkul.items():
    print(f"- {matakuliah}: {rata2}")

print("\n\n")

rata_rata_mhs = rata_rata_mahasiswa(nama, nilai_matkul)
print("==============================================")
print("2. Rata-rata nilai untuk setiap mahasiswa:")
print("==============================================")
for mahasiswa, rata2 in rata_rata_mhs.items():
    print(f"- {mahasiswa}: {rata2}")
