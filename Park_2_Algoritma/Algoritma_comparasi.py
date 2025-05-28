x = 2
y = 2
# besar
hasil = (x > y)
print(f"Hasil dari komper antara {x} besar dari {y} adalah {hasil}")
# besar sama dengan
hasil = (x >= y)
print(f"Hasil dari komper antara {x} besar dari sama dengan {y} adalah {hasil}")
# kecil
hasil = (x < y)
print(f"Hasil dari komper antara {x} kecil dari {y} adalah {hasil}")
# kecil sama dengan
hasil = (x <= y)
print(f"Hasil dari komper antara {x} kecil dari sama dengan {y} adalah {hasil}")

x = "Benar"
y = "benar"
# apakah nilai nya sama (==)
hasil = (x == y)
print(f"Hasil dari komper antara {x} sama dengan  {y} adalah {hasil}")

# not itu kebalikan dari keadaan saat ini 
kondisi = True
hasil = (kondisi != False) # ! atau not : hasil dari kebalikan apapun 
print(f"Apa kah nilai dari hasil : {hasil}")

# and , or , xor , xand  
# kondisi1 dan(and) kondis2 harus tepenuhi  
# and 
hasil = (x != y) and (kondisi != False)
print(f"Sisi kiri dan kanan nilainya : {hasil}")