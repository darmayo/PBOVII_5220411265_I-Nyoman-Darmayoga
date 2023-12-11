#kelompok 12

class Animal: #Pembuatan grandparent 
    hewan_masuk = []
    def __init__(self,nama,sifat,ukuran,jumlah_kaki) -> None:
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran 
        self.jumlah_kaki = jumlah_kaki
    
    def tambah_hewan(self,jenis_aves = None,bisa_terbang = None,jenis_mamalia = None ,bisa_jalan = None,jenis_ayam = None, bisa_diadu = None,jenis_merpati = None): # polimorfisme (overloading)
        if jenis_aves is not None:
            if jenis_ayam is not None:
                Animal.hewan_masuk.append([self.nama,self.sifat,self.ukuran,self.jumlah_kaki,jenis_aves,bisa_terbang,jenis_ayam,bisa_diadu])
            elif jenis_merpati is not None:
                Animal.hewan_masuk.append([self.nama,self.sifat,self.ukuran,self.jumlah_kaki,jenis_aves,bisa_terbang,jenis_merpati])
            else:
                Animal.hewan_masuk.append(["aves",self.nama,self.sifat,self.ukuran,self.jumlah_kaki,jenis_aves,bisa_terbang])
        elif jenis_mamalia is not None:
            Animal.hewan_masuk.append(["mamalia",self.nama,self.sifat,self.ukuran,self.jumlah_kaki,jenis_mamalia,bisa_jalan])
            
    def __list_hewan(): # Pembuatan private function 
        print("=============Semua Hewan===============")
        for i in range(len(Animal.hewan_masuk)):
            if Animal.hewan_masuk[i][0] == "mamalia":
                print(f"{i+1}.Nama          = {Animal.hewan_masuk[i][1]}")
                print(f"  Sifat         = {Animal.hewan_masuk[i][2]}")
                print(f"  Ukuran        = {Animal.hewan_masuk[i][3]}")
                print(f"  Jumlah Kaki   = {Animal.hewan_masuk[i][4]}")
                print(f"  Jenis Mamalia = {Animal.hewan_masuk[i][5]}")
                print(f"  Bisa Jalan    = {Animal.hewan_masuk[i][6]}")
                print()
            elif Animal.hewan_masuk[i][0] == "aves":
                print(f"{i+1}.Nama         = {Animal.hewan_masuk[i][1]}")
                print(f"  Sifat        = {Animal.hewan_masuk[i][2]}")
                print(f"  Ukuran       = {Animal.hewan_masuk[i][3]}")
                print(f"  Jumlah Kaki  = {Animal.hewan_masuk[i][4]}")
                print(f"  Jenis Aves   = {Animal.hewan_masuk[i][5]}")
                print(f"  Bisa Terbang = {Animal.hewan_masuk[i][6]}")
                print()
            elif len(Animal.hewan_masuk[i]) == 8:
                print(f"{i+1}.Nama         = {Animal.hewan_masuk[i][0]}")
                print(f"  Sifat        = {Animal.hewan_masuk[i][1]}")
                print(f"  Ukuran       = {Animal.hewan_masuk[i][2]}")
                print(f"  Jumlah Kaki  = {Animal.hewan_masuk[i][3]}")
                print(f"  Jenis Aves   = {Animal.hewan_masuk[i][4]}")
                print(f"  Bisa Terbang = {Animal.hewan_masuk[i][5]}")
                print(f"  Jenis Ayam   = {Animal.hewan_masuk[i][6]}")
                print(f"  Bisa Diadu   = {Animal.hewan_masuk[i][7]}")
                print()
            elif len(Animal.hewan_masuk[i]) == 7:
                print(f"{i+1}.Nama         = {Animal.hewan_masuk[i][0]}")
                print(f"  Sifat        = {Animal.hewan_masuk[i][1]}")
                print(f"  Ukuran       = {Animal.hewan_masuk[i][2]}")
                print(f"  Jumlah Kaki  = {Animal.hewan_masuk[i][3]}")
                print(f"  Jenis Aves   = {Animal.hewan_masuk[i][4]}")
                print(f"  Bisa Terbang = {Animal.hewan_masuk[i][5]}")
                print(f"  Jenis Ayam   = {Animal.hewan_masuk[i][6]}")
                print()

    def tampil_semua(): # Mengakses function private (akses modifier)
        Animal.__list_hewan()

class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki,jenis_mamalia,bisa_jalan) -> None:
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.jenis_mamalia = jenis_mamalia
        self.bisa_jalan = bisa_jalan
    
    def insert(self): # polimorfisme (overiding)
        super().tambah_hewan(jenis_mamalia = self.jenis_mamalia,bisa_jalan = self.bisa_jalan)

class Aves(Animal): # Pembuatan parent inheritance dari class Animal
    def __init__(self, nama, sifat, ukuran, jumlah_kaki,jenis_aves,bisa_terbang) -> None:
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.jenis_aves = jenis_aves
        self.bisa_terbang = bisa_terbang  
    def insert(self,jenis_ayam = None, bisa_diadu = None,jenis_merpati = None): # polimorfisme (overiding)
        if jenis_ayam != None:
            super().tambah_hewan(jenis_aves = self.jenis_aves,bisa_terbang = self.bisa_terbang,jenis_ayam= jenis_ayam, bisa_diadu=bisa_diadu)
        elif jenis_merpati != None:
            super().tambah_hewan(jenis_aves = self.jenis_aves,bisa_terbang = self.bisa_terbang,jenis_merpati= jenis_merpati)
        else:
            super().tambah_hewan(jenis_aves = self.jenis_aves,bisa_terbang = self.bisa_terbang)

class Ayam(Aves):#Pembuatan child inheritance dari class Aves
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, jenis_aves, bisa_terbang,jenis_ayam,bisa_diadu) -> None:
        super().__init__(nama, sifat, ukuran, jumlah_kaki, jenis_aves, bisa_terbang)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu
    def insert(self):
        return super().insert(jenis_ayam=self.jenis_ayam, bisa_diadu=self.bisa_diadu)

class Merpati(Aves):#Pembuatan child inheritance dari class Aves
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, jenis_aves, bisa_terbang,jenis_merpati) -> None:
        super().__init__(nama, sifat, ukuran, jumlah_kaki, jenis_aves, bisa_terbang)
        self.jenis_merpati = jenis_merpati
    def insert(self): # polimorfisme (overiding)
        return super().insert(jenis_merpati=self.jenis_merpati)

# Pembuatan Object
gagak = Aves("Roger","Pemimpin","Sedang",2,"Elang",True)
gajah = Mamalia("Bobby","Pintar","Besar",4,"Gajah",True)
bangkok = Ayam("Robinhood","Pemberani","kecil",2,"Ayam",True,"Bangkok",True)
dara = Merpati("Cantika","Setia","kecil",2,"Merpati",True,"Merpati Putih")
# Pemanggilan method pada object
gagak.insert()
gajah.insert()
bangkok.insert()
dara.insert()
# Pemanggilan class tanpa object
Animal.tampil_semua()