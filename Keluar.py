def menu():
    while True:
        print("\n#Buat Menu")
        print("#1. Keluar")
        
        pilihan = input("Pilih menu (1): ")
        
        if pilihan == '1':
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

menu()