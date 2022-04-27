import datetime

def load_data():
    data = {}
    data_rekening = open("data_rekening.txt")
    for line in data_rekening:
        nama, nohp, email, amount = line.split(',')
        data[nama] = [nohp, email, int(amount)]

    data_transfer = open("data_transfer.txt")
    for line in data_transfer:
        nama, waktu, amount, description = line.split(',')
        data[nama][2] += int(amount)

    return data

def account_exist(name):
    data = open("data_rekening.txt")
    for line in data:
        nama, nohp, email, amount = line.split(',')
        if nama == name:
            return True
    return False

def check_account(nama):
    data_transfer = open("data_transfer.txt")
    for line in data_transfer:
        if nama in line:
            return False
    return True

def create_account(nama, nohp, email):
    if (check_account(nama)):
        f = open("data_rekening.txt", "a")
        f.write(f"{nama},{nohp},{email},0\n")
        f.close()
        print(f"Akun dengan nama {nama} berhasil dibuat")
    else:
        print("Terdapat akun dengan nama yang sama.")

def get_balance(nama):
    data = load_data()
    return int(data[nama.title()][2])

def check_funds(nama, amount):
    return get_balance(nama) >= amount

def pengeluaran(nama, amount, description):
    if (check_funds(nama, amount)):
        f = open("data_transfer.txt", "a")
        f.write(f"{nama},{datetime.datetime.now().strftime('%x %X')},{-amount},{description}\n")
        f.close()
    else:
        print("Saldo tidak mencukupi")

def deposit(nama, amount):
    f = open("data_transfer.txt", "a")
    f.write(f"{nama},{datetime.datetime.now().strftime('%x %X')},{amount},Deposit\n")
    f.close()
    print(f"Deposit sejumlah {amount}")

def transfer(nama, amount, tujuan):
    if (check_funds(nama, amount)):
        f = open("data_transfer.txt", "a")
        f.write(f"{nama},{datetime.datetime.now().strftime('%x %X')},{-amount},Transfer ke {tujuan}\n")
        f.write(f"{tujuan},{datetime.datetime.now().strftime('%x %X')},{amount},Transfer dari {nama}\n")
        f.close()
        print(f"Transfer sejumlah {amount} ke {tujuan}")
    else:
        print("Saldo tidak mencukupi")

def transaksi_akun(nama, jenis, range):
    data_rekening = open("data_transfer.txt")
    for line in data_rekening:
        name, time, amount, description = line.split(',')
        tanggal, waktu = time.split()
        new_description = description.rstrip('\n')
        if nama == name:
            if ((range == 'harian') & (tanggal == datetime.datetime.now().strftime("%x"))):
                if (((jenis == 'penerimaan') & (int(amount) >= 0))):
                    print(f"{tanggal} {waktu} {new_description} sejumlah Rp.{int(amount)}")
                elif (((jenis == 'pengeluaran') & (int(amount) < 0))):
                    print(f"{tanggal} {waktu} {new_description} sejumlah Rp.{-int(amount)}")
            elif ((range == 'mingguan') & (datetime.datetime.strptime(tanggal,'%x').isocalendar()[1] == datetime.datetime.now().isocalendar()[1])):
                if (((jenis == 'penerimaan') & (int(amount) >= 0))):
                    print(f"{tanggal} {waktu} {new_description} sejumlah Rp.{int(amount)}")
                elif (((jenis == 'pengeluaran') & (int(amount) < 0))):
                    print(f"{tanggal} {waktu} {new_description} sejumlah Rp.{-int(amount)}")
            elif ((range == 'bulanan') & (datetime.datetime.strptime(tanggal,'%x').strftime("%m") == datetime.datetime.now().strftime("%m"))):
                if (((jenis == 'penerimaan') & (int(amount) >= 0))):
                    print(f"{tanggal} {waktu} {new_description} sejumlah Rp.{int(amount)}")
                elif (((jenis == 'pengeluaran') & (int(amount) < 0))):
                    print(f"{tanggal} {waktu} {new_description} sejumlah Rp.{-int(amount)}")

def informasi_akun(nama):
    name = nama.title()
    data = load_data()
    print("\n=== INFORMASI AKUN ===")
    print(f"Nama    : {name}")
    print(f"No. HP  : {data[name][0]}")
    print(f"Email   : {data[name][1]}")
    print(f"Saldo   : {data[name][2]}\n")