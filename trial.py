# namaLengkap = input("Nama Lengkap: ")
# nrp = input("NRP: ")
# tempatTanggalLahir = input("Tempat dan Tanggal Lahir: ")
# noTelp = input("Nomor Telepon: ")
# email = input("E-mail(tanpa @gmail.com): ")

# namaPanggilan = namaLengkap.split()[0]
# digitNrp = nrp[-3:]
# noTelpForm = noTelp[:4] + "-" + noTelp[4:8] + "-" + noTelp[8:]
# emailLengkap = email + "@gmail.com"

# print(f"Nama Lengkap: {namaLengkap}")
# print(f"Nama Panggilan: {namaPanggilan}")
# print(f"3 Digit Terakhir NRP: {digitNrp}")
# print(f"Tempat dan Tanggal Lahir: {tempatTanggalLahir}")
# print(f"Nomor Telepon: {noTelpForm}")
# print(f"E-mail Lengkap: {emailLengkap}")
def ulang_tahun():
    from itertools import cycle
    import random, string
    
    kata = [
        "".join([chr(c) for c in [115,101,108,97,109,97,116]]), 
        "".join(["117","108","97","110"]).encode().decode("utf-8"), 
        "g_tahun".replace("_",""), 
        "kak", 
        ''.join(random.choice("riyan") for _ in range(5)),  
        "selamat",
        "berkepala",
        str(int("1")+int("1")),
        ":bensin_abis:",
        "sticker"
    ]
    
    hasil = []
    for idx, k in enumerate(cycle(kata)):
        hasil.append(k)
        if idx == 9: break
    return " ".join(hasil[:5]) + " " + " ".join(hasil[5:])

print(ulang_tahun())