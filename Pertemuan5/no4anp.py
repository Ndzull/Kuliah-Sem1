hargaAsli=float(input("Harga yang harus dibayar: Rp."))
diskon=float(input("Diskon yang didapatkan(masukan desimal persentase contoh: 0.1): "))
hargaSetelahDiskon=int(hargaAsli*(1-diskon))
print(f"Harga Asli\t\t= Rp.{int(hargaAsli)}")
print(f"Diskon \t\t\t= {int(diskon*100)}%")
print(f"Harga setelah diskon \t= {hargaSetelahDiskon}")

