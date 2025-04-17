print("=== program nilai ===")
nilai = int(input("masukan nilai: "))

if nilai >= 80:
    print ("selamat, anda lulus!")

print ("tetap semangat, tingkatkan nilai kedepannya")

username = input("masukan username: ")
password = input("masukan password: ")

if username == 'ilyas' and password == 'admin':
    print("masuk ke aplikasi")
elif username == 'ilyas' and password != 'admin':
    print("password anda salah")
else:
    print("username dan password salah")


print("== program selesai ==")