import datetime #liblary (javascript atau python) atau header (C,C++,C#) atau pakage (java)

tanggal_dibuat = datetime.datetime.now() #format nya menggunakan format UTC kalau gak pakai curentmillisecon
nama_atasn = "Gea Saskia"
nama_perusahaan = "PT Ruang Keahlian"
alamat_perusahaan  = "Ruangguru HQ, Jl. Dr. Saharjo No. 161, Manggarai Selatan, Tebet, Jakarta Selatan.  "
#posisonal argumen
print("==========Posisional Argument==========")
print("\t\t{0}\nYTH.IBU/BAPAK {1}\nManager SDM {2}\n{3}".format(tanggal_dibuat,nama_atasn,nama_perusahaan,alamat_perusahaan))
print("==========Keyword Argument==========")
print("\t\t{tanggal}\nYTH.IBU/BAPAK {nama}\nManager SDM {nama_pt}\n{alamat}".format(alamat = alamat_perusahaan , nama = nama_atasn , tanggal = tanggal_dibuat,nama_pt = nama_perusahaan))
print("==========Format Argument==========")
print(f"\t\t{tanggal_dibuat}\nYTH.IBU/BAPAK {nama_atasn}\nManager SDM {nama_perusahaan}\n{alamat_perusahaan}")