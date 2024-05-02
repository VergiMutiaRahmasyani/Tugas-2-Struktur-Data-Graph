class Peta:
    def __init__(self):
        self.daftarKota = {}

    def printPeta(self):
        for kota in self.daftarKota:
            print(kota, ":", self.daftarKota[kota])

    def tambahKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = []
            return True
        return False

    def printKota(self):
        for kota in self.daftarKota:
            print(f"{kota} -- {self.daftarKota[kota]}")

    def tambahJalan(self, kota1, kota2):
        if kota1 in self.daftarKota and kota2 in self.daftarKota:
            # Tambahkan kota2 ke daftar kota1
            self.daftarKota[kota1].append(kota2)
            # Tambahkan kota1 ke daftar kota2
            self.daftarKota[kota2].append(kota1)
            return True
        return False

petaIrlandia = Peta()

daftarKota = {
    'Castlebar': ['Tuam', 'Galway'],
    'Tuam': ['Castlebar', 'Galway'],
    'Galway': ['Tuam', 'Ennis', 'Athlone'],
    'Ennis': ['Galway', 'Limerick'],
    'Limerick': ['Ennis', 'Portlaoise', 'Kilkenny'],
    'Athlone': ['Galway', 'Mullingar', 'Portlaoise'],
    'Mullingar': ['Athlone', 'Ireland'],
    'Portlaoise': ['Naas', 'Limerick', 'Athlone', 'Kilkenny'],
    'Naas': ['Portlaoise', 'Carlow', 'Ireland'],
    'Carlow': ['Naas', 'Kilkenny'],
    'Kilkenny': ['Carlow', 'Portlaoise'],
}

# Inisialisasi peta dengan daftar kota dan jalur yang diberikan
for kota, jalur in daftarKota.items():
    petaIrlandia.tambahKota(kota)
    for tujuan in jalur:
        petaIrlandia.tambahJalan(kota, tujuan)

# Hapus kota tertentu dari peta berdasarkan input pengguna
print("Kota yang tersedia untuk dihapus:", list(petaIrlandia.daftarKota.keys()))
kota_yang_dihapus = input("Masukkan nama kota yang ingin dihapus: ")
if petaIrlandia.hapusKota(kota_yang_dihapus):
    print("Kota", kota_yang_dihapus, "telah dihapus dari peta.")
else:
    print("Kota", kota_yang_dihapus, "tidak ditemukan dalam peta.")

# Print peta setelah penghapusan
petaIrlandia.printPeta()
