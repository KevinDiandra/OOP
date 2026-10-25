class Wario:
    def __init__(self, nama):
        self.nama = nama
        self.nyawa = 2
        self.skor = 0
        self.is_moving = True

    def bergerak(self):
        self.is_moving = True
        print(f"-----{self.nama} Mulai Bergerak!-----")

    def skor_stage(self,jumlah):
        self.skor += jumlah
        print(f"{self.nama} mengambil {jumlah} koin!")
        print(f"Skor sekarang: {self.skor}")

    def mengenai_objek(self, nama_objek):
        if nama_objek == "Kura-kura":
            self.nyawa -= 1
            print(f"Terkena Damage! Nyawa tersisa: {self.nyawa}")
            if self.nyawa == 0:
                print("Game Over!")
        else:
            print(f"{self.nama} mengenai {nama_objek}!")

    def info_player(self):
        print(f"-----Selamat Anda Telah Menyelesaikan Stage!-----")
        print(f"Hasil Skor Akhir: {self.skor}")

wario = Wario("Wario")
wario.bergerak()

# wario mengenai kura-kura
wario.mengenai_objek("Kura-kura")
wario.skor_stage(556)
wario.info_player()