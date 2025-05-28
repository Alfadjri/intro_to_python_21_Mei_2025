# nilai siswa

print("=========if======")
#di pakai saat kamu mau belokin rumus atau arah 
nilai = 50
if nilai >= 70:
    print("Nilai kamu lulus dengan pas-pas-san")
    
print("=========if else========")
# harus tau kalau misalnya terjadi masalah kamu harus ngapain
if nilai >= 70:
    print("Nilai kamu lulus dengan pas-pas-san")
else:
    print("Kamu tidak lulus")

print("=========Tenery========")
nilai = 70
# variabel = nilaiTrue if kondisi else nilaiFalse
pesan = "Lulus" if nilai > 70 else "tidak lulus" #yang ini di sebut tenery  (excel,php,java,c) (kondisi) ? benar : salah
print(pesan)

print("======if elif else ===========")
nilai = 40
if nilai >= 90:
    print("Lulus Sempurna")
elif nilai > 70 and nilai <= 80:
    print("Hampir tidak lulus")
else : #kasus lain atau default
    print("Tidak lulus")

# switch case atau match case (python)
# kita udah tau apa yang akan di lakukan user 
print("==============switch case=========")
print("-------Menu--------")
print("1.Start")
print("2.End")
select = input("Selection(1,2) => ")
match select:
    case "1":
        print("Start")
    case "2":
        print("End")
    case _ :
        print("invalid input please input 1 or 2")