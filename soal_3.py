class Queue:
    def __init__(self):
        self.antrian = []

    def enqueue(self, nama, menu):
        pesanan = {'nama': nama, 'menu': menu}
        self.antrian.append(pesanan)
        print("==================================")
        print(f"Pesanan '{menu}' untuk '{nama}' ditambahkan ke dalam antrian.")
        print("==================================")

    def dequeue(self):
        if len(self.antrian) < 1:
            return "Antrian kosong"
        pesanan = self.antrian.pop(0)
        print("==================================")
        print(f"Pesanan '{pesanan['menu']}' untuk '{pesanan['nama']}' dihapus dari antrian.")
        print("==================================")
        return pesanan

    def data_pelanggan(self):
        if not self.antrian:
            print("Antrian kosong")
        else:
            for index, pesanan in enumerate(self.antrian, start=1):
                print(f"{index}. {pesanan['nama']} - {pesanan['menu']}")
            print("==================================")
