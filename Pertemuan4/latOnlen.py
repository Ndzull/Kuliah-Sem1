#1
a=8
b=3
c=12
print((a>b) and (c%a==4)) #8>3 and 4==4
print((b**2<=a) or (c//b>4)) #9<=8 or 4>4
#2
harga=3500000
hargadiskon=harga*0.9
unit=80-3
pendapatantotal=hargadiskon*unit
print(f"Pendapatan toko tersebut adalah: {int(pendapatantotal)}")
#3
nama=input("Masukkan namamu: ")
umur=input("Umurmu berapa: ")
print(f"Halo, nama saya {nama}, umur saya {umur} tahun")
#4
str="shape of you"
str1=str[0:9].rstrip()
print(str1)
print(len(str1))
