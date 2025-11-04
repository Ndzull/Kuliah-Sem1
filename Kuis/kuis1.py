# Nama: Naila Dzulfa
# NRP: 2043251046
# Kelas: B Statistika Bisnis
# Kuis 1 Algoritma dan Pemrograman
# Saya berani bersaksi bahwa saya mengerjakan ini dengan jujur tanpa bantuan dari AI.


#no 1
#a
hargaBeli=float(input("Masukan harga beli per unit: ")) #input harga belinya, pakai float karena contoh input: 2.000
hargaJual=float(input("Masukan harga jual per unit: ")) #input harga jualnya, pakai float karena contoh input: 2.000
jumlahBarang=int(input("Masukan jumlah barang terjual: ")) #input jumlah barang yang terjual, pakai int karena jumlah barang adalah angka bulat, contoh input: 3
biayaOperasional=float(input("Masukan biaya operasional tambahan: ")) #input biaya operasional, pakai float karena contoh input: 2.000
#b
totalModal= hargaBeli*jumlahBarang #menghitung total modal dari harga beli dikalikan sebanyak jumlah barang
totalPendapatan=hargaJual*jumlahBarang #menghitung total pendapatan yaitu harga jual dikalikan jumlah barang
untungRugi=totalPendapatan-(totalModal+biayaOperasional) #mencari keuntungan/kerugian, total pendapatan dikurang total biaya yang diperlukan
#c
print(f"Total modalnya: {totalModal:.3f}") #setiap output saya gunakan .3f agar terlihat ribuan
print(f"Total pendapatannya: {totalPendapatan:.3f}")
if(untungRugi<=0):      #saya pakai condition karena untuk membedakan input jika - dan + alias jika rugi dan untung dan ketika tidak sama sekali
    print(f"Nilai kerugian: {untungRugi:.3f}") 
elif(untungRugi>=0):
    print(f"Nilai keuntungan: {untungRugi:.3f}")
else:
    print("Tidak untung dan tidak rugi")

#no 2
data = [[10, 20, 30, 40, 50, 60], ["alpha", "beta", "gamma", "delta", "epsilon"], [100, "theta", 200, "lambda", 300]] 
#a
hasil=[]
hasil.extend(data[0][-3:]) #saya menggunakan extend karena outputnya ingin list tunggal
hasil.extend(data[1][1:3])
hasil.extend(data[2][0:5:2])
#b
print(hasil)

#no 3
import statistics #saya menggunakan library statistics agar mempermudah perhitungan statistika yang ada disini, karena library ini memuat fungsi statistika seperti mean,median,standar deviasi dan lain-lain
data=[]
nom=float(input("Masukan nilai ke-1: ")) #saya buat masukan manual untuk menambahkan input variabel nom masuk ke list data yang telah saya buat
data.append(nom)
nom=float(input("Masukan nilai ke-2: "))
data.append(nom)
nom=float(input("Masukan nilai ke-3: "))
data.append(nom)
nom=float(input("Masukan nilai ke-4: "))
data.append(nom)
nom=float(input("Masukan nilai ke-5: "))
data.append(nom)
nom=float(input("Masukan nilai ke-6: "))
#a
mean=statistics.mean(data)
print(f"{mean:.2f}")
median=statistics.median(data)
print(f"{median:.2f}")
maxNom=max(data)
minNom=min(data)
jangkauan=maxNom-minNom
print(f"{jangkauan:.2f}") #menggunakan .2f untuk memunculkan 2 angka belakang koma
#b
data.remove(maxNom)
mean2=statistics.mean(data)
stdev=statistics.stdev(data)
print(f"{stdev:.2f}")

# no 4
angka = [12, 25, 37, 49, 53, 68, 72, 84, 91, 105]
# a. [105, 91, 84, 72, 68, 53, 49, 37, 25, 12]
angka.reverse()
print(angka)

# no 4
angka = [12, 25, 37, 49, 53, 68, 72, 84, 91, 105]
#b. [25, 49, 68, 84, 105] 
print(angka[1:10:2])

# no 4
angka = [12, 25, 37, 49, 53, 68, 72, 84, 91, 105]
#c. [105, 91, 84] 
angka=angka[-3:]
angka.reverse()
print(angka)

# no 4
angka = [12, 25, 37, 49, 53, 68, 72, 84, 91, 105]
#d.[12, 37, 53, 72, 91, 25, 49, 68, 84, 105] 
print(angka[0:10:2]+angka[1:10:2])

# no 4
angka = [12, 25, 37, 49, 53, 68, 72, 84, 91, 105]
#e. [72, 68, 53, 49, 37]
angka=angka[-8:-3]
angka.reverse()
print(angka)