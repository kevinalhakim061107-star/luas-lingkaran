import math

jari_jari = float(input("Masukkan nilai jari-jari: "))

print("Pilihan:")
print("1. Hitung keliling lingkaran")
print("2. Hitung luas lingkaran")
pilihan = int(input("Masukkan angka pilihan (1/2): "))

if pilihan == 1:
    keliling = 2 * math.pi * jari_jari
    print("Keliling lingkaran =", keliling)
elif pilihan == 2:
    luas = math.pi * jari_jari ** 2
    print("Luas lingkaran =", luas)
else:
    print("Pilihan tidak valid, masukkan angka 1 atau 2.")        