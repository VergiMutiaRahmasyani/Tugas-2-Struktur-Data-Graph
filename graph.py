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
