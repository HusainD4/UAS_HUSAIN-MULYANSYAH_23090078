class Queue:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print("===="*20)
        print(f"Pesanan '{pesanan}' ditambahkan ke dalam antrian.")
        print("===="*20)

    def dequeue(self):
        if len(self.antrian) < 1:
            return "Antrian kosong"
        pesanan = self.antrian.pop(0)
        print("===="*20)
        print(f"Pesanan '{pesanan}' dihapus dari antrian.")
        print("===="*20)
        return pesanan

    def display(self):
        if not self.antrian:
            print("Antrian kosong")
        else:
            print("===="*20)
            print("Data antrian pelanggan:")
            print("===="*20)
            for index, pesanan in enumerate(self.antrian, start=1):
                print(f"{index}. {pesanan}")
