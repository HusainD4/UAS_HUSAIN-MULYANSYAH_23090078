me = "HUSAIN MULYANSYAH"
no = "23090078"

print(f"NAMA\t: {me},\nNIM\t:{no}\n")

# Kelas Parent: Buah
class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    
    def setNama(self, nama):
        self.nama = nama
    
    def setWarna(self, warna):
        self.warna = warna
    
    def setRasa(self, rasa):
        self.rasa = rasa
    
    def information(self):
        return f"Nama: {self.nama}, \nWarna: {self.warna}, \nRasa: {self.rasa}"

# Kelas Child: Mangga
class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        Buah.__init__(self, nama, warna, rasa)
        self.vitamin = vitamin
    
    def setVitamin(self, vitamin):
        self.vitamin = vitamin
    
    def setInformation(self):
        info = Buah.information(self)
        return f"{info}, Vitamin: {self.vitamin}"

mangga1 = Mangga("Mangga Arumanis", "Hijau", "Manis", "Vitamin C")
print("==========================================================")
print("output dari kelas parent")
print("==========================================================")
print(mangga1.information())      
print("==========================================================")
print("\n==========================================================")
print("output dari kelas child")
print("==========================================================")
print(mangga1.setInformation())   
mangga1.setVitamin("Vitamin A")
print("==========================================================")
print("\n==========================================================")
print("output setelah mengubah vitamin")
print("==========================================================")
print(mangga1.setInformation())   
print("==========================================================")
