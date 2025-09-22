#16
film="the great gatsby".title()[:10].rstrip()
print(film,len(film))
#17
str=input("Masukan String: ")
print(str[:-1], str[1:])
print(str[1:-1])
#18
firstName="Thomas"
middleName="Alva"
lastName="Edison"
yearOfBirth="1847"
namaLengkap=firstName+" "+middleName+" "+lastName
print(f"Tahun kelahiran {namaLengkap} adalah {yearOfBirth}")
#latpenutup
name=input("Please enter your full name: ")
num=len(name.replace(" ",""))
print(f"Hello {name}! Your name has {num} letters, excluding spaces.")
