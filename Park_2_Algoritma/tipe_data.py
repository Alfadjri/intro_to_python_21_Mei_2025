# int
# bilangan bulat 
x = 32767 #banyak digit
print("ini contoh tipe data Intenger {0}".format(x))
# float
# bilangan desimal (bilangan berkoma)
x = 9.8
print("ini contoh tipe data float {0}".format(x))
# kompleks
x = 2 + 3j
print("ini contoh tipe data kompleks {0}".format(x))

#sqyence type
a = [1,2,3,4,5,5,6,7,8,9,0,0,12,3,23,3,2,23,223,2] #list
print("ini contoh tipe data list {0}".format(a))
b = (4,5,6) #truplet ini tipe data yang tidak bisa di ubah
print("ini contoh tipe data truplet {0}".format(b))
c = range(2) #range di gunakan untuk menulis urutan 
# format dasar range(start,end,langkah)
print("ini contoh tipe data {0}".format(c))

#tipe data non primitif
#String dapat menampung sebanyak char[255] 255 jumlah digit
nama = "Alfadjri" #contoh
print("ini contoh tipe String {0}".format(nama))

#maping type
#dic
profile = {"nama" : "alfajri","age":24}
print("ini contoh tipe dictionary {0}".format(profile))


#Set type
f = {1,2,3} #set
print("ini contoh tipe dictionary {0}".format(f))
g = frozenset({2,3,4,5,6})
print("ini contoh tipe frozenset {0}".format(g))

#Tipe data boolean
#tipe data yang nilainya hanya ada 2  True(1) atau False(0)
kondisi = 1
kondisi_conversi = bool(kondisi)
kondisi_manual = True
kondisi_manual_conversi = int(kondisi_manual)
print("Ini contoh tipe data boolean using simbol : {0}".format(kondisi))
print("Ini contoh tipe data boolean conversi : {0}".format(kondisi_conversi))
print("Ini contoh tipe data boolean manual : {0}".format(kondisi_manual))
print("Ini contoh tipe data boolean manual to integer : {0}".format(kondisi_manual_conversi))


# binary
i = 0b01000010
# desimal = int(i)
# print("Angka binary ke desimal {0}".format(desimal))
# char = chr(desimal)
# print("Angka binary ke karakter {0}".format(char))
print("Angka binary ke karakter {0}".format(chr(int(i))))
j = bytearray(a)
print("byte yang ada pada data A : {0}".format(j))
k = memoryview(j)
print("lokasi dari list yang di simpan di memory(ram) {0}".format(k))

