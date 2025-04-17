print("menentukan kelulusan")
nama = input("nama mahasiswa: ")
nilai_uts = int(input("masukan nilai UTS:"))
nilai_uas = int(input("masukan nilai UAS:"))
if nilai_uas>=90 :
    if nilai_uts>=80 :
        print('selamat', nama,'anda lulus')
    else:
        print(nama,'lulus, lebih giat belajar ya')
else:
    print(nama,'anda belum lulus')