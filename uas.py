import random

class ToDoList:
    def __init__(self):
        self.tasks = []  
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tugas '{task}' berhasil ditambahkan!\n")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Tugas '{task}' berhasil dihapus!\n")
        else:
            print(f"Tugas '{task}' tidak ditemukan!\n")
    
    def show_tasks(self):
        if not self.tasks:
            print("Belum ada tugas dalam daftar.\n")
        else:
            print("\nDaftar Tugas:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
            print()
    
    def random_task(self):
        if self.tasks:
            print(f"Tugas acak yang dipilih: {random.choice(self.tasks)}\n")
        else:
            print("Daftar tugas kosong!\n")

def main():
    todo = ToDoList()
    
    while True:
        print("=== MENU TO-DO LIST ===")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Lihat Tugas")
        print("4. Pilih Tugas Acak")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            task = input("Masukkan tugas baru: ").strip()
            todo.add_task(task)
        
        elif pilihan == "2":
            task = input("Masukkan tugas yang ingin dihapus: ").strip()
            todo.remove_task(task)
        
        elif pilihan == "3":
            todo.show_tasks()
        
        elif pilihan == "4":
            todo.random_task()
        
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    main()
