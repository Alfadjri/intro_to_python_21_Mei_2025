from Manager import Manager

def main():
    list_data = [
        {
            "nama_kariawan" : "Alfadjri Dwi Fadhilah",
            "usia" : 24,
            "pekerjaan" : "Cybersecurity",
            "gaji" : 8500000,
            "jumlah_tim" : 0
        },
        {
            "nama_kariawan" : "Toni",
            "usia" : 24,
            "pekerjaan" : "Programmer",
            "gaji" : 8000000,
            "jumlah_tim" : 2
        },
        {
            "nama_kariawan" : "Siti",
            "usia" : 24,
            "pekerjaan" : "Ui and UX",
            "gaji" : 5500000,
            "jumlah_tim" : 5
        },
    ]
    print("=====List Kariawan======")
    for person in list_data:
        manager = Manager(person["nama_kariawan"],person["usia"],person["pekerjaan"],person["gaji"],person["jumlah_tim"])
        print(manager.getDetail())
        print("========Work========")
        print(manager.work())
        print("====================")
        print()
    
    

if __name__ == "__main__":
    main()