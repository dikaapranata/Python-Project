import datetime

class Account:
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.ledger = list()
    
    def deposit(self, amount, desc=''):
        if (desc == ''):
            self.ledger.append({"date": datetime.datetime.now(), "amount": amount, "description": f"Deposit"})
        else:
            self.ledger.append({"date": datetime.datetime.now(), "amount": amount, "description": desc})

    def withdraw(self, amount, desc=''):
        if (self.check_funds(amount)):
            if (desc == ''):
                self.ledger.append({"date": datetime.datetime.now(), "amount": -amount, "description": f"Pengeluaran"})
            else:
                self.ledger.append({"date": datetime.datetime.now(), "amount": -amount, "description": desc})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def check_funds(self, amount):
        if (amount > self.get_balance()):
            return False
        else:
            return True
    
    def transfer(self, amount, destination):
        if (self.check_funds(amount)):
            self.withdraw(amount, f"Transfer ke {destination.name}")
            destination.deposit(amount, f"Terima transfer dari {self.name}")
    
    def show_transaction(self, category, jangkaWaktu):
        if (category == 'pengiriman'):
            text = "Transaksi Pengiriman "
            if (jangkaWaktu == 'harian'):
                text += "Harian"
                print(text)
                for item in self.ledger:
                    if (item["amount"] >= 0 and item["date"].strftime("%m/%d/%Y") == datetime.datetime.now().strftime("%m/%d/%Y")):
                        print(f"{item['description']} sebesar Rp.{item['amount']} pada {item['date'].strftime('%m/%d/%Y %H:%M')}")
            elif (jangkaWaktu == 'mingguan'):
                text += "Mingguan"
                print(text)
                for item in self.ledger:
                    if (item["amount"] >= 0 and item["date"].isocalendar()[1] == datetime.datetime.now().isocalendar()[1]):
                        print(f"{item['description']} sebesar Rp.{item['amount']} pada {item['date'].strftime('%m/%d/%Y %H:%M')}")
            elif (jangkaWaktu == 'bulanan'):
                text += "Bulanan"
                print(text)
                for item in self.ledger:
                    if (item["amount"] >= 0 and item["date"].strftime("%m/%Y") == datetime.datetime.now().strftime("%m/%Y")):
                        print(f"{item['description']} sebesar Rp.{item['amount']} pada {item['date'].strftime('%m/%d/%Y %H:%M')}")
        elif (category == 'pengeluaran'):
            text = "Transaksi Pengeluaran "
            if (jangkaWaktu == 'harian'):
                text += "Harian"
                print(text)
                for item in self.ledger:
                    if (item["amount"] < 0 and item["date"].strftime("%m/%d/%Y") == datetime.datetime.now().strftime("%m/%d/%Y")):
                        print(f"{item['description']} sebesar Rp.{-item['amount']} pada {item['date'].strftime('%m/%d/%Y %H:%M')}")
            elif (jangkaWaktu == 'mingguan'):
                text += "Mingguan"
                print(text)
                for item in self.ledger:
                    if (item["amount"] < 0 and item["date"].isocalendar()[1] == datetime.datetime.now().isocalendar()[1]):
                        print(f"{item['description']} sebesar Rp.{-item['amount']} pada {item['date'].strftime('%m/%d/%Y %H:%M')}")
            elif (jangkaWaktu == 'bulanan'):
                text += "Bulanan"
                print(text)
                for item in self.ledger:
                    if (item["amount"] < 0 and item["date"].strftime("%m/%Y") == datetime.datetime.now().strftime("%m/%Y")):
                        print(f"{item['description']} sebesar Rp.{-item['amount']} pada {item['date'].strftime('%m/%d/%Y %H:%M')}")
                
    def __str__(self):
        return f'Nama: {self.name}\nNomor HP: {self.phoneNumber}\nBalance: {self.get_balance()}\n'

acc1 = Account("Andi", "12312312", "Andi@gmail.com")
acc2 = Account("Budi", "321312", "Budi@gmail.com")

acc1.deposit(50000, 'Tes')
# acc1.withdraw(1000, 'Belanja')
# acc1.withdraw(1000, '')
print(acc1)
print(acc2)
acc1.transfer(1000, acc2)
print(acc1)
print(acc2)
acc1.show_transaction('pengeluaran', 'harian')
