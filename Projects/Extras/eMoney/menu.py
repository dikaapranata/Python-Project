import function as f

def menu_awal():
    print("Selamat datang di e-Money")
    print("Pilih menu berikut untuk lanjut")
    print("1. Masuk")
    print("2. Daftar")
    print("0. Keluar")
    input_key = ''
    while (input_key != '1' and input_key != '2' and input_key != '0'):
        input_key = input("Masukkan pilihan: ")
        if (input_key == '1'):
            print("\n==== Masuk ====")
            menu_masuk()
        elif (input_key == '2'):
            print("\n==== Daftar ====")
            menu_daftar()
        elif (input_key == '0'):
            print("Terima kasih sudah menggunakan layanan ini.")
            exit()
        else:
            print("Masukkan sesuai pilihan!")

def menu_masuk():
    nama = input('Masukkan namamu: ')
    if (f.account_exist(nama)):
        menu_utama(nama)
    else:
        print("Akun tidak tersedia!")
        print("1. Coba lagi")
        print("0. Kembali")
        input_key = ''
        while (input_key != '1' and input_key != '0'):
            input_key = input("Masukkan pilihan: ")
            if (input_key == '1'):
                menu_masuk()
            elif (input_key == '0'):
                menu_awal()
            else:
                print("Masukkan sesuai pilihan!")

def menu_utama(nama):
    print(f'\nHallo {nama}, Selamat datang!')
    print("\n=== MENU UTAMA ===")
    print("1. Deposit")
    print("2. Belanja")
    print("3. Transfer")
    print("4. History Transaksi")
    print("5. Informasi Akun")
    print("0. Keluar")
    menu = ['0', '1', '2', '3', '4', '5']
    input_key = ''
    while input_key not in menu:
        input_key = input("Masukkan pilihan: ")
        if (input_key == '1'):
            menu_deposit(nama)
        elif (input_key == '2'):
            menu_belanja(nama)
        elif (input_key == '3'):
            menu_transfer(nama)
        elif (input_key == '4'):
            history_transaksi(nama)
        elif (input_key == '5'):
            informasi_akun(nama)
        elif (input_key == '0'):
            print("Terima kasih sudah menggunakan layanan ini.")
            exit()
        else:
            print("Masukkan sesuai pilihan!")

def menu_daftar():
    nama = input("Masukkan nama: ")
    if (f.account_exist(nama)):
        print("Akun sudah ada!")
        print("1. Masuk")
        print("2. Coba lagi")
        print("0. Kembali")
        exist_input = ''
        while exist_input not in ('0', '1', '2'):
            exist_input = input("Masukkan pilihan: ")
            if (exist_input == '1'):
                menu_utama(nama)
            if (exist_input == '2'):
                menu_daftar()
            elif (exist_input == '0'):
                menu_awal()
    else:
        no_hp = input("Masukkan Nomor HP: ")
        email = input("Masukkan Email: ")
        f.create_account(nama, no_hp, email)
        menu_utama(nama)

def menu_deposit(nama):
    print(f"Deposit ke akun {nama}")
    amount = int(input("Masukkan nominal deposit: "))
    f.deposit(nama, amount)
    transaksi_lagi(nama)

def menu_belanja(nama):
    tujuan = input("Masukkan tujuan belanja: ")
    amount = int(input("Masukkan nominal pengeluaran: "))
    f.pengeluaran(nama, amount, tujuan)
    transaksi_lagi(nama)

def menu_transfer(nama):
    tujuan = input("Masukkan tujuan transfer: ")
    if (f.account_exist(tujuan)):
        amount = int(input("Masukkan nominal transfer: "))
        f.transfer(nama, amount, tujuan)
        transaksi_lagi(nama)
    else:
        print("Akun tidak ditemukan.")
        transaksi_lagi(nama)

def history_transaksi(nama):
    header = "\n=== HISTORY TRANSAKSI "
    pilihan_jenis = ['0', '1','2']
    pilihan_range = ['0', '1', '2', '3']
    print("Pilih jenis transaksi")
    print("1. Penerimaan")
    print("2. Pengeluaran")
    print("0. Kembali")
    input_jenis = ''
    while input_jenis not in pilihan_jenis:
        input_jenis  = input("Masukkan pilihan: ")
    if input_jenis == '0':
        menu_utama(nama)
    
    print("Pilih waktu transaksi")
    print("1. Harian")
    print("2. Mingguan")
    print("3. Bulanan")
    print("0. Kembali")
    input_range = ''
    while input_range not in pilihan_range:
        input_range  = input("Masukkan pilihan: ")
    if input_range == '0':
        menu_utama(nama)

    if (input_jenis == '1'):
        header += "PENERIMAAN "
        if (input_range == '1'):
            header += "HARIAN ==="
            print(header)
            f.transaksi_akun(nama, 'penerimaan', 'harian')
        elif (input_range == '2'):
            header += "MINGGUAN ==="
            print(header)
            f.transaksi_akun(nama, 'penerimaan', 'mingguan')
        else:
            header += "BULANAN ==="
            print(header)
            f.transaksi_akun(nama, 'penerimaan', 'bulanan')
    else:
        header += "PENGELUARAN "
        if (input_range == '1'):
            header += "HARIAN ==="
            print(header)
            f.transaksi_akun(nama, 'pengeluaran', 'harian')
        elif (input_range == '2'):
            header += "MINGGUAN ==="
            print(header)
            f.transaksi_akun(nama, 'pengeluaran', 'mingguan')
        else:
            header += "BULANAN ==="
            print(header)
            f.transaksi_akun(nama, 'pengeluaran', 'bulanan')
    print("\n")
    transaksi_lagi(nama)

def transaksi_lagi(nama):
    print("Apakah ingin transaksi lagi?")
    print("1. Ya")
    print("0. Tidak")
    menu = ['0', '1']
    input_key = ''
    while input_key not in menu:
        input_key = input("Masukkan pilihan: ")
        if (input_key == '1'):
            menu_utama(nama)
        elif (input_key == '0'):
            print("Terima kasih sudah menggunakan layanan ini.")
            exit()
        else:
            print("Masukkan sesuai pilihan!")

def informasi_akun(nama):
    f.informasi_akun(nama)
    transaksi_lagi(nama)