#20
namaTim=input("Masukan nama Tim Baseball: ")
jmlMenang=int(input("Jumlah pertandingan yang dimenangkan: "))
jmlKalah=int(input("Jumlah pertandingan yang kalah"))
totalPertandingan=jmlMenang+jmlKalah
persentase=(jmlMenang/totalPertandingan)*100
print(f"Nama Tim: {namaTim}")
print(f"Persentase kemenangan: {int(persentase)}%")
