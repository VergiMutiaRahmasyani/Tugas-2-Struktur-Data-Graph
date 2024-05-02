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
