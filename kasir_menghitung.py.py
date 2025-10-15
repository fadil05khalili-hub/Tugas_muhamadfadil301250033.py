# Minta pengguna masukin total belanja
total_belanja = float(input("Masukkan total belanja kamu (Rp): "))

# Bagian ini buat ngitung diskon sesuai ketentuan
# Aku pakai if-elif biar jelas urutannya

if total_belanja >= 500000:
    diskon = 0.20  # Diskon 20% kalau belanja di atas 500 ribu
elif total_belanja >= 250000:
    diskon = 0.10  # Diskon 10% kalau belanja di atas 250 ribu tapi belum sampai 500 ribu
else:
    diskon = 0     # Kalau belanja di bawah 250 ribu ya belum dapet diskon, sabar dulu :)

# Sekarang kita hitung jumlah diskonnya
potongan = total_belanja * diskon

# Lalu hitung total yang harus dibayar setelah diskon
total_bayar = total_belanja - potongan

# Tampilkan hasilnya biar pengguna tahu semuanya
print("\n===== STRUK PEMBAYARAN =====")
print(f"Total Belanja : Rp {total_belanja:,.0f}")  # format biar ada koma
print(f"Diskon        : Rp {potongan:,.0f}")
print(f"Total Bayar   : Rp {total_bayar:,.0f}")
print("=============================")