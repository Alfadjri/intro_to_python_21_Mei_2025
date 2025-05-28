x = 3
y = 2

# Penjumlahan
hasil = x + y
print(f"Hasil dari {x} + {y} = {hasil}")
hasil = x - y
print(f"Hasil dari {x} - {y} = {hasil}")
hasil = x * y
print(f"Hasil dari {x} * {y} = {hasil}")
hasil = x / y
print(f"Hasil dari {x} / {y} = {hasil}")
hasil = int(x / y) #conversion
print(f"Hasil dari {x} / {y} = {hasil}")
hasil = x // y
print(f"Hasil dari {x} // {y} = {hasil}")
# modulus (%) : sisa dari pembagian 
hasil = x % y
print(f"Hasil dari {x} % {y} = {hasil}")


# x = x + 1 (ini teknik junior)
#incremnet
# teknik ini di pakai saat kita mau pakai variabel yang sama
x += 100 #  di jabarkan x = x + 1
print(f"Nilai dari x saat ini : {x}")
#decerment
x -= 1 #  di jabarkan x = x -1
print(f"Nilai dari x saat ini : {x}")


keliling = 10 + 10 + 10


harga_awal = 10000
diskon = 20
total_disokn = (1000 * 20) / 100
total_harga = harga_awal + total_disokn
print(f"Total harga setelah di diskon : {total_harga}")