from soal_3 import Queue

me = "HUSAIN MULYANSYAH"
no = "23090078"

print(f"NAMA\t: {me},\nNIM\t:{no}\n")

def kelola():
    queue = Queue()
    print("=========================================")
    print('data yang tertambahkan')
    print("=========================================")
    queue.enqueue("ANDI")
    queue.enqueue("BUDI")
    queue.enqueue("HUSAIN")
    
    print("\n=========================================")
    print('dmenampilkan data antrian saat ini')
    print("=========================================")
    queue.data_antrian()
    
    print("\n=========================================")
    print('data yang sudah terhapus')
    print("=========================================")
    queue.dequeue()
    queue.dequeue()
    
    print("\n=========================================")
    print('\ndmenampilkan data antrian saat ini')
    print("=========================================")
    queue.data_antrian()
    
kelola()




