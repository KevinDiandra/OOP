# class Commander: # membuat  class
# 	def __init__(self, nama, role, hp, attack_power, gold): #class construktor
# 		self.nama = nama
# 		self.hp = hp
# 		self.attack_power = attack_power #properties
# 		self.role = role
# 		self.gold = gold

# 	def serang(self, target):
# 		damage = self.attack_power
# 		target.terima_dammage(damage)
# 		print(f" {self.nama} menyerang {target.nama} sebesar {damage} DMG ")

# 	def terima_damage(self, jumlah):
# 		self.hp -= jumlah
# 		if self.hp < 0:
# 			self.hp = 0

# 	def masih_hidup(self):
# 		return self.hp > 0 

# 	def dapatkan_gold(self, jumlah):
# 		self.gold += jumlah
# 		print(f"{self.nama} mendapatkan {jumlah} gold. Total gold: {self.gold}")

# k1 = Commander("Commander A", "Tank", 100, 20, 50)
# k2 = Commander("Commander B", "DPS", 80, 30, 30)


# k1.dapatkan_gold(50)
# k2.dapatkan_gold(70)

# print(f"{k1.nama} (HP: {k1.hp}, Role: {k1.role}, Gold: {k1.gold})")
# print(f"{k2.nama} (HP: {k2.hp}, Role: {k2.role}, Gold: {k2.gold})")

# class KatakZuma:
# 	def __init__(self, warna_awal):
# 		# TODO: skor, is_active
# 		self.warna_peluru = warna_awal
# 		self.skor = 0
# 		self.is_active = True

# 	def ganti_warna(self, warna_baru):
# 		warna_lama = self.warna_peluru
# 		self.warna_peluru = warna_baru
# 		print(f"{warna_lama} berganti menjadi {warna_baru}")

# k1 = KatakZuma("Kuning")
# k1.ganti_warna("Biru")

# print(f"Warna peluru saat ini: {k1.warna_peluru}")

# print(f"Skor: {k1.skor}")

# print(f"Status: {'Aktif' if k1.is_active else 'Tidak Aktif'}")

class KarakterSurfer:
	def __init__(self,nama):
		self.nama = nama
		self.skor = 0
		self.koin = 0
		self.is_running = True

	def berlari(self):
		self.is_running = True
		print(f"-----{self.nama} Mulai berlari!-----")

	def ambil_koin(self,jumlah):
		self.koin += jumlah
		print(f"Jumlah Koin Saat Ini = {self.koin}")

	def tabrak_rintangan(self):
		self.is_running = False
		print(f"-> {self.nama} Menabrak Kereta!")

	def info_player(self):
		print("-----Info Player Saat Ini!-----")
		print(f"Nama		: {self.nama}")
		print(f"Jumlah Koin	: {self.koin}")
		print(f"Status Berlari	: {self.is_running}")

	def info_player_final(self):
		print("-----Game Over!-----")
		print("-> Info Akhir Player!")
		print(f"Nama		: {self.nama}")
		print(f"Jumlah Koin	: {self.koin}")
		print(f"Status Berlari	: {self.is_running}")

player1 = KarakterSurfer("Angel")

player1.info_player()

player1.berlari()
player1.ambil_koin(100)
player1.tabrak_rintangan()

player1.info_player_final()