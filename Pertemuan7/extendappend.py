angka=[4,3,2,6]
teks=["a","b","c","d"]
angka.extend([7,1])
print(angka)
#[4, 3, 2, 6, 7, 1]
angka.append([7,1])
print(angka)
#[4, 3, 2, 6, [7, 1]]
