profile = [
    {
        "nama" : "Alfadjri Dwi Fadhilah",
        "age" : 24,
        "pekerjaan" : "IT Support"
    },
    {
        "nama" : "Toni",
        "age" : 24
    },
    {
        "nama" : "budi",
        "age" : 24
    }
]
print(f"Nama : {profile[0]["nama"]}")
print(f"Usia : {profile[0]["age"]}")
print(f"Pekerjaan : {profile[0]["pekerjaan"]}")
print(f"Nama : {profile[1]["nama"]}")
print(f"Usia : {profile[1]["age"]}")
print(f"Nama : {profile[2]["nama"]}")
print(f"Usia : {profile[2]["age"]}")
print("============Setelah di singikat============")

# mempersinkat ini 
# function 
# void : sifatnya function yang tidak memiliki aksi apapun 
def cetak_nilai(nama,usia,pekerjaan = None):
    print(f"Nama : {nama}")
    print(f"Usia : {usia}")
    print(f"Pekerjaan : {pekerjaan}")

# Cara panggil
cetak_nilai(profile[0]["nama"],profile[0]["age"],profile[0]["pekerjaan"])
cetak_nilai(profile[1]["nama"],profile[1]["age"])
cetak_nilai(profile[2]["nama"],profile[2]["age"])

# return keluarkan hasil dari function 
def penjumlahan(a,b):
    return a + b

# cara panggilnya
hasil = penjumlahan(10,10)
print(f"Hasil dari 10 + 10 = {hasil}")