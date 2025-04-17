def kalkulator():
    print("Selamat Datang di Kalkulator Looping!")
    print("Operasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")

    while True:
        try:
            pilihan = input("Masukkan nomor operasi (1-5): ")
            if pilihan == '5':
                print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
                break
            
            pilihan = int(pilihan)
            if pilihan < 1 or pilihan > 5:
                print("Pilihan tidak valid. Silakan masukkan nomor antara 1 dan 5.")
                continue
        except ValueError:
            print("Masukan tidak valid. Silakan masukkan nomor.")
            continue

        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Masukan angka tidak valid. Silakan coba lagi.")
            continue

        if pilihan == 1:
            hasil = num1 + num2
            print(f"Hasil: {num1} + {num2} = {hasil}")
        elif pilihan == 2:
            hasil = num1 - num2
            print(f"Hasil: {num1} - {num2} = {hasil}")
        elif pilihan == 3:
            hasil = num1 * num2
            print(f"Hasil: {num1} * {num2} = {hasil}")
        elif pilihan == 4:
            if num2 == 0:
                print("Kesalahan: Pembagian dengan nol tidak diizinkan.")
            else:
                hasil = num1 / num2
                print(f"Hasil: {num1} / {num2} = {hasil}")
        
        print()  

kalkulator()