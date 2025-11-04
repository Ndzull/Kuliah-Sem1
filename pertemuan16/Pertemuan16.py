#Naila Dzulfa B Statistika Bisnis
#2043251046
#ALPRO 4 November 2025
#Halaman 125
#File alternatif (barangkali ipynbnya tidak bisa dibuka)

#no 3
PLANE_RIDE_COST=200 #deklarasi variabel PLANE_RIDE_COST yang berisi nilai 200
def main(): #buat fungsi main
    noOfDays=3 #deklarasi variabel noOfDays yang berisi nilai 3
    cost=PLANE_RIDE_COST+noOfDays*20 #Buat variabel baru (cost) untuk menyimpan perhitungan variabel PLANE_RIDE_COST ditambah noOfDays dikali 20 (perhitungan sesuai prioritas)
    print("Total cost: {0:,.2f}".format(cost)) #menampilkan hasil 200+3*20=200+60=260 dengan format desimal dengan 2 angka dibelakang koma (makanya jadi 260.00)
main() #panggil fungsi main untuk memanggil perhitungan didalamnya dan outputnya
# Output
# Total cost: 260.00

#no 6
def perkenalan(nama, departemen, fakultas):
    print(f"Halo! Nama saya {nama}! Dari Departemen {departemen} Fakultas {fakultas}")
def biodata(tanggalLahir, tempatLahir, kos):
    print(f"Tanggal lahir saya {tanggalLahir}, saya asli {tempatLahir}, dan sekarang saya ngekos di {kos}")

perkenalan("Ijul","Statistika Bisnis","Vokasi")
biodata("29 November 2007", "Cirebon", "Mulyosari")
# Output
# Halo! Nama saya Ijul! Dari Departemen Statistika Bisnis Fakultas Vokasi
# Tanggal lahir saya 29 November 2007, saya asli Cirebon, dan sekarang saya ngekos di Mulyosari

#no 7
def data(nama,nrp):
    print(f"Saya {nama}, NRP {nrp}")

print("Masukan Nama Panggilan dan NRP")
nama,nrp=input().split()
data(nama,nrp)
# Output
# Masukan Nama Panggilan dan NRP
# Saya ijul, NRP 2043251046

#versi nama lengkap
def data(nama,nrp):
    print(f"Saya {nama}, NRP {nrp}")

nama=input("Masukan namamu: ")
nrp=input("NRP mu: ")
data(nama,nrp)
# Output
# Saya Naila Dzulfa, NRP 2043251046


