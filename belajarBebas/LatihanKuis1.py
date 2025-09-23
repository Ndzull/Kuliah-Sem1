#spoil no 1
d=float(input("berapa diameter dari lingkaran: "))
pi=3.14
r=d/2
luasLingkaran=pi*(r**2)
print(f"Luas lingkaran: {luasLingkaran}")
#Luas lingkaran: 38.465

#spoil no 2 a berbagai cara
angka=[]
num=int(input("Angka pertama: "))
angka.append(num)
num=int(input("Angka kedua: "))
angka.append(num)
num=int(input("Angka ketiga: "))
angka.append(num)
num=int(input("Angka keempat: "))
angka.append(num)
num=int(input("Angka kelima: "))
angka.append(num)
angka.remove(1)
angka.append(32)
print(angka)

angka=[]
num=1
for i in range(6):
    angka.append(num)
    num=num*2
del angka[0]
print(angka)

angka=[1,2,4,8,16]
angka.remove(1)
angka.append(32)
print(angka)
#[2, 4, 8, 16, 32]

#spoil no 2 b
angka=[7,32,81,20,25,14,23,27]
print(angka[::2]+angka[-1:])
#[7, 81, 25, 23, 27]

#spoil no 2 c
angka=['A','k','u',' ','j','u','a','r','a']
print("".join(angka))
#Aku juara

#spoil no 3
import math
a=164.70/1.3
b=154.54/1.3
c=176.64/1.3
d=143.23/1.3
e=149.38/1.3
n=5
mean=(a+b+c+d+e)/n
print(f"{mean:.2f}")
var=(((a-mean)**2)+((b-mean)**2)+((c-mean)**2)+((d-mean)**2)+((e-mean)**2))/n-1
print(f"{var:.2f}")
std=math.sqrt(var)
print(f"{std:.2f}")
# 121.31
# 81.40
# 9.02

#spoil no 3
import statistics
a=164.70/1.3
b=154.54/1.3
c=176.64/1.3
d=143.23/1.3
e=149.38/1.3
angka=[a,b,c,d,e]
mean=statistics.mean(angka)
print(f"{mean:.2f}")
var=statistics.variance(angka)
print(f"{var:.2f}")
std=statistics.stdev(angka)
print(f"{std:.2f}")
# 121.31
# 103.00
# 10.15

#no 4 pake tabulasi horizontal
print("No\tNegara\t\tindex inflasi")
print("1\tIndonesia\t3.98")
print("2\tMalaysia\t4.70")
print("3\tSingapura\t2.42")
# No	Negara		index inflasi
# 1	Indonesia	3.98
# 2	Malaysia	4.70
# 3	Singapura	2.42

print("{0:^3s}{1:<20s}{2:<15s}".format("No","Negara","Index inflasi"))
print("{0:^3s}{1:<20s}{2:<15n}".format("1","Indonesia",3.98))
print("{0:^3s}{1:<20s}{2:<15s}".format("2","Malaysia","4.70")) #biar 0 e gahilang wkwkw
print("{0:^3s}{1:<20s}{2:<15n}".format("3","Singapura",2.42))
# No Negara              Index inflasi  
#  1 Indonesia           3.98           
#  2 Malaysia            4.70           
#  3 Singapura           2.42           

str1="mahasiswa teladan"
str2="statistika bisnis ITS"
gabungan=str1[0:9]+str2[-10:]
print(gabungan)
#mahasiswabisnis ITS

import statistics
import math
angka=(3.13,3.56,3.10,2.88,3.67)
semua=statistics.fsum(angka)
akhir=math.sqrt(semua)
print(akhir)
#4.042276586281547
