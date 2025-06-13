file = open("./../Write/Contoh_Text_Save.txt","r")
value_all = file.read()
print(value_all)
# readline
file.seek(0)
print(f"Ambil value sampai index ke 3 : {file.readline(3)}")

# ambil 1 baris 
# readlines
file.seek(0)
for row in file.readlines():
    print(row.strip())
    break

file.close()