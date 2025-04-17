import math

def menu():
    while True:
        print("\n#Buat Menu")
        print("#1. Program Luas Lingkaran")
        print("#2. Keluar")
        
        pilihan = input("Pilih menu (1/2): ")
        
        if pilihan == '1':
            radius = float(input("Masukkan jari-jari lingkaran: "))
            luas = math.pi * radius * radius
            print(f"Luas lingkaran dengan jari-jari {radius} adalah {luas:.2f}")
        elif pilihan == '2':
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

menu()
