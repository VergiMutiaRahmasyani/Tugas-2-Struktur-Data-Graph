from itertools import permutations

class WeightedGraph:
    def __init__(self):
        #Inisialisasi untuk menyimpan daftar kota dan jalur
        self.daftarKota = {}

    def printPeta(self):
        #Mencetak daftar kota berdasarkan jalur
        for kota in self.daftarKota:
            print(kota, ":", self.daftarKota[kota])
            for neighbor, distance in self.daftarKota[kota].items():
                #print tetangga dan jarak
                print("    ->", neighbor, ":", distance)

    def tambahkanKota(self, kota):
        #Menambahkan kota baru ke dalam peta jika belum ada
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
            return True
        return False
    
    def hapusKota(self, kotaDihapus):
        # Mengecek kota yang ingin dihapus ada di list
        if kotaDihapus in self.daftarKota:
            #Iterasi kepada setiap kota lain untuk menghapus kota yang akan dihapus
            del self.daftarKota[kotaDihapus]
            for kota in self.daftarKota:
                #Mengecek kota yang ingin dihapus apakah ada jalannya ke kota lain
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self, kota1, kota2, jarak):
        #Mengecek apakah kota1 dan kota2 ada dalam list
        if kota1 in self.daftarKota and kota2 in self.daftarKota:
            #Tambahkan kota2 ke daftar kota1 dan sebaliknya
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak
            return True
        return False

    def hapusJalan(self, kota1, kota2):
        if kota1 in self.daftarKota and kota2 in self.daftarKota:
            if kota2 in self.daftarKota[kota1]:
                #Hapus jalur antara dua kota
                self.daftarKota[kota1][kota2]
            if kota1 in self.daftarKota[kota2]:
                self.daftarKota[kota2][kota1]
            return True
        return False
