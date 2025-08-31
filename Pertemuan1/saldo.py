#mencari saldo
#ver. pemula
saldo=100
saldo2=saldo+(saldo*0.05)+100
saldo3=saldo2+(saldo2*0.05)+100
saldoakhir=saldo3+saldo3*0.05
print(f"nilai keseimbangannya adalah:{(round(saldoakhir,2))}")
#ver. pemula extend
saldo=100
i=0
for i in range(2):
    saldo=saldo*0.05+saldo+100
    i+1

saldo=saldo+saldo*0.05
print(f"nilai keseimbangannya adalah:${(round(saldo,2))}")
