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

    def dijkstra(self, source):
        #Membuat map untuk mengetahui jarak dari setiap kota ke sumber
        distances = {}
        for city in self.daftarKota:
            distances[city] = float('inf')
            
        #Menentukan jarak ke number 0
        distances[source] = 0
        
        print (distances)
        
        unvisited_cities = []
        for city in self.daftarKota:
            unvisited_cities.append(city)
        print (unvisited_cities)

        while unvisited_cities:
            # Mencari kota terdekat dengan jarak minimun
            min_distance = float('inf')
            closest_city = None
            #mengiterasi setiap kota yang belum dikunjungi
            for city in unvisited_cities:
                #jika jarak kota lebih kecil dari min_distance
                if distances[city] < min_distance:
                    min_distance = distances[city]
                    closest_city = city

            #Menghapus vertex u dari kota yang belum dikunjungi
            unvisited_cities.remove(closest_city)

            #Update nilai jarak dari semua vertx yang berdekatan
            for neighbor, weight in self.daftarKota[closest_city].items():
                #jika jarak kota terdekat + bobot lebih kecil dari jarak kota tetangga, maka ubah nilai distance
                distance = distances[closest_city] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances
        
    def tsp(self):
        shortest_distance = float('inf')
        shortest_path = []


        cities = list(self.daftarKota.keys())
        for path in permutations(cities):
            total_distance = 0
            for i in range(len(path) - 1):
                if path[i] in self.daftarKota and path[i + 1] in self.daftarKota[path[i]]:
                    total_distance += self.daftarKota[path[i]][path[i + 1]]
                else:
                    total_distance = float('inf')
                    break  
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = path

        return shortest_path, shortest_distance


# Example usage with Dijkstra's algorithm:
petaIrlandia = WeightedGraph()
petaIrlandia.tambahkanKota("Castlebar")
petaIrlandia.tambahkanKota("Tuam")
petaIrlandia.tambahkanKota("Galway")
petaIrlandia.tambahkanKota("Ennis")
petaIrlandia.tambahkanKota("Limerick")
petaIrlandia.tambahkanKota("Athlone")
petaIrlandia.tambahkanKota("Mullingar")
petaIrlandia.tambahkanKota("Portlaoise")
petaIrlandia.tambahkanKota("Naas")
petaIrlandia.tambahkanKota("Carlow")
petaIrlandia.tambahkanKota("Kilkenny")
petaIrlandia.tambahkanKota("Ireland")

petaIrlandia.tambahkanJalan("Castlebar", "Tuam", 55)
petaIrlandia.tambahkanJalan("Castlebar", "Galway", 75)
petaIrlandia.tambahkanJalan("Galway", "Ennis", 74)
petaIrlandia.tambahkanJalan("Ennis", "Limerick", 3)
petaIrlandia.tambahkanJalan("Limerick", "Kilkenny", 130)
petaIrlandia.tambahkanJalan("Kilkenny", "Carlow", 37)
petaIrlandia.tambahkanJalan("Carlow", "Portlaoise", 40)
petaIrlandia.tambahkanJalan("Porlaoise", "Naas", 56)
petaIrlandia.tambahkanJalan("Naas", "Mullingar", 74)
petaIrlandia.tambahkanJalan("Mullingar", "Ireland", 4)
petaIrlandia.tambahkanJalan("Ireland", "Athlone", 24)
petaIrlandia.tambahkanJalan("Athlone", "Tuam", 94)

petaIrlandia.printPeta()
shortest_distances = petaIrlandia.dijkstra("Castlebar")
print("Shortest distances from Seoul to other cities:")
for city, distance in shortest_distances.items():
    print(city, ":", distance)
shortest_path, shortest_distance = petaIrlandia.tsp()
print("Shortest TSP path:", shortest_path)
print("Shortest TSP distance:", shortest_distance)



