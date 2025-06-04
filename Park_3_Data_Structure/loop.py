# while
# di pakai saat syaratnya di ketahui tapi gak tau jalan untuk memenuhi syrat tersebut
# dia akan di check dulu baru di kerjakan
print("==========While===========")
count = 2001
while count <= 2000:
    print(f"Index of {count}")
    count += 1

#do while
#di pakai saat ingin di kerjakan dulu baru di check


# for
# di pakai saat kamu tau jalan untuk sampai tujuan 
print("==========for===========")
for value in range(0,2001):
    print(f"Index of {value}")
    
# case list
makanans = ['Ikan', 'mie', 'Nasi', 'Semangka', 'Melon',"Pisang"]
# format 
# for variabel_sementara in data_value_list :
    # yang akan di lakukan dalam 1 putaran

for value in makanans:
    print(f"Value of : {value}") # satu section atau loop 
    print(f"Value putaran")

print("==========break and countinue===========")

count = 1
while count <= 100:
    if count % 2 == 0 :
        count += 1
        continue # untuk skip atau melewati 1 putaran penuh
    
    print(f"{count}")
    count+=1
    
    if count >= 30:
        break # ini untuk menghentikan secara paksa semua putaran