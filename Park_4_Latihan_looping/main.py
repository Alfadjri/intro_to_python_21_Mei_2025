import os # ini di sebut liblary (python) , java (pakage) , c++(header)
# import os ini liblary untuk check sistem operasi apa yang kita gunakan
import platform

def clear_terminal():
    os_name = platform.system()
    if os_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def error_input(pesan = "Input yang anda masukan tidak sesuai"):
    input(pesan)
    
def persegi():
    clear_terminal()
    sisi = int(input("Jumlah Sisi yang akan di buat : "))
    for i in range(sisi+1):
        for j in range(sisi+1):
            print("*",end=" ")
        print()
    print()



def segitiga_siku_siku_kiri_bawah(banyak_baris):
    for i in range(banyak_baris+1):
        for j in range(i+1):
            print("*",end=" ")
        print()
    print()  


def segitiga_siku_siku_kanan_atas(banyak_baris):
    for i in range(banyak_baris,0,-1):
        for j in range(banyak_baris-i):
            print(" ",end=" ")
        for k in range(i):
            print("*",end=" ")
        print()
    print()
    
def menu_segitiga():
    clear_terminal()
    banyak_baris = 5
    pesan_next = "Tekan Enter untuk balik ke menu awal"
    print("==========Segitiga========")
    print("1.Kiri bawah")
    print("2.Kanan Atas")
    print("q.Back")
    select = input("Select => ")
    match select:
        case "1":
            segitiga_siku_siku_kiri_bawah(banyak_baris)
            error_input(pesan_next)
        case "2":
            segitiga_siku_siku_kanan_atas(banyak_baris)
            error_input(pesan_next)
        case "q":
            return
        case _ :
            error_input()
            menu_segitiga()


def main():
    pesan_next = "Tekan Enter untuk balik ke menu awal"
    while True:
        clear_terminal()
        print("==========Menu========")
        print("1.Persegi")
        print("2.Segitiga Siku-siku")
        print("q.Quit")
        select = input("Select => ")
        match select:
            case "1" :
                persegi()
                error_input(pesan_next)
            case "2":
                menu_segitiga()
            case "q" :
                print("Selamat Tinggal")
                break
            case _:
                error_input()

if __name__ == "__main__":
    main()