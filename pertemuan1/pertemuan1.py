# '''def cobafungsi(a):
#     b=a+3
#     return b

# a=int(input('coba input sesuatu:'))
# print(f"hasil penjumlahan: {cobafungsi(a)}")'''

# '''a=int(input('berapapun: '))

# if(a==5):
#     print("Adalah lima")
# elif(a==6):
#     print("Adalah 6")
# elif(a!=1):
#     print("Yang jelas bukan 1")'''

# '''saldo=100
# saldo2=saldo+(saldo*0.05)+100
# saldo3=saldo2+(saldo2*0.05)+100
# saldoakhir=saldo3*0.05
# print(f"nilai keseimbangannya adalah:{(round(saldoakhir,2))}")'''
# '''nama=input("masukkan nama: ")

# if(nama=="reval"):
#     print("wong gendeng")
# elif(nama=="mas amar"):
#     print("sedang tidur")
# elif(nama=="hani"):
#     print("roben sedang mengetik...")
# elif(nama=="ketzia"):
#     print("gwanteng")
# else:
#     print("siapa")'''

answer=input("masukkan angka: ")
guess=input("tebaklah angka: ")

if(guess==answer):
    print("Cogratulation! Your guess is correct!")
while(guess!=answer):
    if(guess>answer):
            print("Your guess is too high!")
            
    elif(guess<answer):
            print("Your guess is too low!")
    guess=input("tebaklah angka: ")

# i=0
# for i in range(8):
#     print("mas amar Jember")
