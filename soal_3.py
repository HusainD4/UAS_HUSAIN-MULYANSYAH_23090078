me = "HUSAIN MULYANSYAH"
no = "23090078"

print(f"NAMA\t: {me},\nNIM\t:{no}\n")

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' di tambahkan.")

    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        order = self.queue.pop(0)
        print(f"Order '{order}' dihapus.")
        return order

    def data_antrian(self):
        print(f"Antrian saat ini: {self.queue}")
