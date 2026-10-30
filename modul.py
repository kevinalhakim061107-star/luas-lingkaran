a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if a > b:
    maksimal = a
elif b > a: 
    maksimal = b
else:
    maksimal = a

print("Angka maksimal =", maksimal)

