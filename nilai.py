print("== masukan angka 1 - 100")
nilai = int(input("masukan nilai: "))

if nilai >= 90 and nilai <= 100 : 
    print("lulus")
    print("grade : A")
elif nilai >= 80 and nilai < 90 :
    print("lulus")
    print("grade B")
elif nilai >= 70 and nilai < 80 :
    print("lulus")
    print("grade C")
elif nilai >= 60 and nilai < 70 : 
    print("tidak lulus, harus mengulang")
    print("grade D")
elif nilai >= 50 and nilai < 60 : 
    print("tidak lulus, harus mengulang")
    print("grade E")
else:
    print("mohon maaf tidak lulus")