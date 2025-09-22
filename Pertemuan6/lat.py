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

print(f"Nama Lengkap\t\t: {namaLengkap}")
print(f"Nama Panggilan\t\t: {namaPanggilan}")
print(f"3 Digit Terakhir NRP\t: {digitNrp}")
print(f"Tempat dan Tanggal Lahir: {tempatTanggalLahir}")
print(f"Nomor Telepon\t\t: {noTelpForm}")
print(f"E-mail Lengkap\t\t: {emailLengkap}")

# Nama Lengkap		: Naila Dzulfa
# Nama Panggilan		: Naila
# 3 Digit Terakhir NRP	: 046
# Tempat dan Tanggal Lahir: Cirebon, 29 November 2007
# Nomor Telepon		: 0882 2049 3181
# E-mail Lengkap		: naiidzull56@gmail.com
