siswa = {
    "kelas" : 12,
    "ketua_kelas" : "Joni",
    "Jurusan" : ["IPA","IPS"],
    "code" : "<h1>Testing</h1>"
}

# Read (R)
print(f"List Data Dicrionary : {siswa}")

# Read Spesifik
print(f"Kelas : {siswa["kelas"]}")
print(f"Nama dari ketua kelas : {siswa["ketua_kelas"]}")
print(f"Saya mau ambil jurusan ips : {siswa["Jurusan"][1]}")

# Add (C)
siswa["mata_pelajaran"] = ["MTK","PPKN","IPS","IPA"]
print(f"List Data Dicrionary : {siswa}")

#Update (U)
siswa["code"] = 404
print(f"List Data Dicrionary : {siswa}")

#Delete (D)
del siswa["mata_pelajaran"]
print(f"List Data Dicrionary : {siswa}")


