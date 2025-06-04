#misal punya data list makanan
# inisialisasi
makanans = ["nasi","mie","ayam"]

# Read all (R)
print(f"Read Data All list : {makanans}")

# Read spesifik value
print(f"value index ke 2 dari data : {makanans[2]}")
print(f"Value index ke -1 dari data : {makanans[-1]}")

#update(U)
makanans[0] = "Ikan"
print(f"Read Data All list after update : {makanans}")

#Create(C)
makanans.append("Nasi")
# makanans.pop("Nasi_tambah")
print(f"Read Data All list after add : {makanans}")

#Delete(D)
makanans.remove("ayam") #coding itu siftanya case sensitif
print(f"Read Data All list after delete : {makanans}")

# bagaimana menggabungkan 2 list
# simbol pagar sebutannya komentar di gunakan untuk menandai code 
makanans += ["Semangka","Melon"]
print(f"Read All Data bahan pokok : {makanans}")