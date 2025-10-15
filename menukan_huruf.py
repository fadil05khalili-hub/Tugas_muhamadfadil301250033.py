# Minta pengguna memasukkan nilai
nilai = int(input("Masukkan nilai angka (0-100): "))

if nilai >= 85 and nilai <= 100:
    print("Nilai huruf kamu adalah: A")  # Nilai tinggi banget, berarti A
elif nilai >= 70:
    print("Nilai huruf kamu adalah: B")  # lumayan bagus, nilainya B
elif nilai >= 55:
    print("Nilai huruf kamu adalah: C")  # Nilaina cukup, tapi masih bisa ditingkatkan
elif nilai >= 40:
    print("Nilai huruf kamu adalah: D")  # Nilainya lumayan rendah
else:
    print("Nilai huruf kamu adalah: E")  # Nilai paling rendah, kudu usaha deui!

# Tambahan sedikit biar nggak kaku
print("makasih saya fadil yang buat masih pemula")
