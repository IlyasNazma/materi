def menu():
    while True:
        print("\n#Buat Menu")
        print("#1. Program Genap Ganjil")
        print("#2. Keluar")
        
        pilihan = input("Pilih menu (1/2): ")
        
        if pilihan == '1':
            angka = int(input("Masukkan angka: "))
            if angka % 2 == 0:
                print(f"{angka} adalah bilangan GENAP")
            else:
                print(f"{angka} adalah bilangan GANJIL")
        elif pilihan == '2':
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

menu()
