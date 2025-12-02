# Nama: Naila Dzulfa
# NRP : 2043251046
# Kelas: B Statistika Bisnis
# KUIS 2 Algoritma dan Pemrograman
# Selasa, 2 Desember 2025

# Saya mengerjakan keseluruhan kuis murni tanpa bantuan AI, dan sesuai dengan ketentuan kuis yang sudah ditetapkan.

#nomor.1
#versi dimana fungsi bongkar benar digunakan untuk "mengurangi" jumlah muatan sampai sesuai dengan kapasitas
class Truk:
    def __init__(self, nama, kapasitas_muatan,muatan_saat_ini): 
        self.nama=nama
        self.kapasitas_muatan=kapasitas_muatan
        self.muatan_saat_ini=muatan_saat_ini
    def muat(self,kg):
        self.kg=kg
        if (self.kg==0):
            print("Input tidak valid")
        else:
            self.muatan_saat_ini+=self.kg
            if (self.muatan_saat_ini>self.kapasitas_muatan):
                print("Overload! Muatan melebihi kapasitas!")
                self.muatan_saat_ini=truk.bongkar()
    def bongkar(self):
        print("Muatan tidak cukup!") #soal ambigu, disini disuruh ngurangin barang sampai muat di kapasitas kan(?)
        while (self.muatan_saat_ini>self.kapasitas_muatan):
            self.muatan_saat_ini-=1
        self.sisa_kapasitas=abs(self.kapasitas_muatan-self.muatan_saat_ini)
        return self.muatan_saat_ini
    def status(self):
        print(f"Nama truk: {self.nama}")
        print(f"Muatan saat ini: {self.muatan_saat_ini} kg")
        print(f"Sisa kapasitas: {self.sisa_kapasitas} kg") #tapi kenapa ada ini?

truk=Truk("Hino", 6000, 1000)
truk.muat(5500)
truk.status()

# nomor.1
#versi ambigu dimana fungsi bongkar hanya untuk mengeluarkan output 
class Truk:
    def __init__(self, nama, kapasitas_muatan,muatan_saat_ini):
        self.nama=nama
        self.kapasitas_muatan=kapasitas_muatan
        self.muatan_saat_ini=muatan_saat_ini
    def muat(self,kg):
        self.kg=kg
        if (self.kg==0):
            print("Input tidak valid")
        else:
            self.muatan_saat_ini+=self.kg
            if (self.muatan_saat_ini>self.kapasitas_muatan):
                print("Overload! Muatan melebihi kapasitas!")
                self.muatan_saat_ini=truk.bongkar()
            else:
                self.sisa_kapasitas=abs(self.kapasitas_muatan-self.muatan_saat_ini)
                truk.status()
    def bongkar(self):
        print("Muatan tidak cukup!") #soal ambigu, disini disuruh ngurangin barang sampai muat di kapasitas kan(?)
        # while (self.muatan_saat_ini>self.kapasitas_muatan):
        #     self.muatan_saat_ini-=1
        self.sisa_kapasitas=self.kapasitas_muatan-self.muatan_saat_ini
        return self.muatan_saat_ini
    def status(self):
        print(f"Nama truk: {self.nama}")
        print(f"Muatan saat ini: {self.muatan_saat_ini} kg")
        print(f"Sisa kapasitas: {self.sisa_kapasitas} kg") #tapi kenapa ada ini? apakah maksudnya method ini ditampilkan dulu lalu panggil method bongkar?

truk=Truk("Hino", 6000, 1000)
truk.muat(5500)
truk.status()

#nomor.2
berat=[2,5,10,3,8]
tarif_per_kg=7000

def hitung_total(berat):
    total=0
    i=0
    # for i in range(1, berat): *salah format perintah sintaks loop 
    for i in range(len(berat)):
        harga=berat[i]*tarif_per_kg #saya menambahkan variabel harga (menghitung harga perpaket) agar bisa menampilkan harga perpaket(lanjut ke line comment total)
        print(f"Paket {i+1}: Rp.{harga}") #tambah untuk output daftar harga
        total+=harga
        #total+=berat[i]*tarif_per_kg *intinya untuk membedakan variabel menyimpan perhitungan perpaket dan total keseluruhan
        i+=1
    return total

#print(hitung_total(berat)) #ini memang bisa mengeluarkan output yang benar, namun belum ada tampilan keterangannya
print(f"Total biaya: Rp.{hitung_total(berat)}")