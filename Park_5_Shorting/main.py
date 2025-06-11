import random #header bahasa C , package in java , libary in python

def generate_random_number(jumlah_data):
    list_data = []
    for value in range(jumlah_data):
        data = random.randint(1,100)
        list_data.append(data)
    return list_data

def bobble_sort(data):
    panjang_data = len(data)
    for i in range(panjang_data):
        for j in range(0,panjang_data-i-1):
            if data[j] > data[j+1]:
                # temp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = temp
                data[j],data[j+1] = data[j+1] , data[j]



                
def select_sort(data):
    panjang_data = len(data)
    for i in range(panjang_data):
        min_index = i
        for j in range(i+1,panjang_data):
            if data[j] < data[min_index]:
                min_index = j
        data[i],data[min_index] = data[min_index] , data[i]

def insertion_sort(data):
    for i in range(1,len(data)):
        nilai = data[i]
        j = i - 1
        while j >= 0 and nilai < data[j] :
            data[j+1] = data[j]
            j -= 1 #decerment 
        data[j+1] = nilai
        
def merge_sort(data):
    if len(data) > 1: #awas ketinggalan kalau ketinggalan ini bisa jadi infinity loop
        mid = len(data) // 2
        kiri = data[:mid]
        kanan = data[mid:]
        
        merge_sort(kiri) # ini di sebut teknik rekursif atau infinity loop
        merge_sort(kanan)
        
        # i = 0
        # j = 0
        # k = 0
        i = j = k = 0
        
        while  i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k+=1
        
        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1
        
        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1
        
        
def main():
    banyak_data = int(input("Banyak Data yang akan di buat : "))
    list_data = generate_random_number(banyak_data)
    print("=====Data yang belum di shorting=====")
    print(list_data)
    input("Tekan Enter untuk melanjutkan prosess ........")
    # bobble_sort(list_data)
    # select_sort(list_data)
    # insertion_sort(list_data)
    merge_sort(list_data)
    print("=====Data yang setelah di shorting=====")
    print(list_data)
    

if __name__ == "__main__":
    main()