# Nama : Naila Dzulfa
# NRP : 2043251046
# Kelas : B Statistika Bisnis

# Halaman 48
#19
n=float(input("Masukan jumlah detik antara petir dan guntur: "))
jarak=n/5
#print(f"Jarak dari badai: {round(jarak,2)}") saya tidak tau kenapa di beberapa compiler/IDE yang saya coba tidak berhasil
#print("Jarak dari badai: ", round(jarak,2))
print(f"Jarak dari badai: {jarak:.2f}")

#20
namaTim=input("Masukan nama Tim Baseball: ")
jmlMenang=int(input("Jumlah pertandingan yang dimenangkan: "))
jmlKalah=int(input("Jumlah pertandingan yang kalah: "))
totalPertandingan=jmlMenang+jmlKalah
persentase=(jmlMenang/totalPertandingan)*100
print(f"Nama Tim: {namaTim}")
print(f"Persentase kemenangan: {int(persentase)}%")

# Halaman 57
#3
print("DAFTAR DEPARTEMEN FAKULTAS VOKASI ITS")
print("-" * 50)
print("{:<30} {:>20}".format("Departemen", "Persentase Mahasiswa"))
print("-" * 50)
print("{:<30} {:<20.1%}".format("Statistika Bisnis", 0.18))
print("{:<30} {:<20.1%}".format("Teknik Infrastruktur Sipil", 0.17))
print("{:<30} {:<20.1%}".format("Teknik Kimia Industri", 0.16))
print("{:<30} {:<20.1%}".format("Teknik Instrumentasi", 0.15))
print("{:<30} {:<20.1%}".format("Teknik Elektro Otomasi", 0.17))
print("{:<30} {:<20.1%}".format("Teknik Mesin Industri", 0.17))

#4
hargaAsli=float(input("Harga yang harus dibayar: Rp."))
diskon=float(input("Diskon yang didapatkan(masukan desimal persentase contoh: 0.1): "))
hargaSetelahDiskon=int(hargaAsli*(1-diskon))
print(f"Harga setelah diskon: {hargaSetelahDiskon}")

#5
pendapatan=float(input("Masukan pendapatan: "))
pengeluaran=float(input("Masukan pengeluaran: "))
labaBersih=int(pendapatan-pengeluaran)
print(f"Laba Bersih Perusahaan: {labaBersih}")