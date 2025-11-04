# print("{:<210}{:>210}".format("Nur Azizah","TUGAS 1"))
# print("{:>105}".format("TUGAS 1"))
namaLengkap=input("Nama Lengkap: ")
nrp=input("NRP: ")
tempatTanggalLahir=input("Tempat dan Tanggal Lahir: ")
noTelp=input("Nomor Telepon: ")
email=input("E-mail(tanpa @gmail.com): ")

n=namaLengkap.rfind(" ")
namaPanggilan=namaLengkap[:n]
digitNrp=nrp[-3:]
noTelpForm = noTelp[:4] + " " + noTelp[4:8] + " " + noTelp[8:]
emailLengkap=email+"@gmail.com"

print(f"Nama Lengkap: {namaLengkap}")
print(f"Nama Panggilan: {namaPanggilan}")
print(f"3 Digit Terakhir NRP: {digitNrp}")
print(f"Tempat dan Tanggal Lahir: {tempatTanggalLahir}")
print(f"Nomor Telepon: {noTelpForm}")
print(f"E-mail Lengkap: {emailLengkap}")

