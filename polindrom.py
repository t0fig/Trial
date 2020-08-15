"""
the biggest polindrom number deriver from mutltiplication of three-digit numbers
"""
z=[]
for a in range(100, 1001):
    for b in range(a, 1001):
        hasil = a * b
        shasil = str(hasil)
        if shasil == shasil[::-1]:
            z.append(hasil)
print(max(z))
