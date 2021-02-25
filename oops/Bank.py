import datetime
class Bank:
    Bank1_name="Union Bank"
    def create_bank(self,acno,name,phno,balance,bank_name):
        self.acno=acno
        self.name=name
        self.phno=phno
        self.balance=balance
        self.bank_name=bank_name
    def deposit_bank(self,amount):
        self.balance+=amount
        print("Your",self.bank_name,Bank.Bank1_name, "account",self.acno, "is credited with",amount,"on",datetime.date.today(),"now your available balace is",self.balance)
    def withdraw_bank(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print("Your",self.bank_name, "account",self.acno, "is debited with",amount,"on",datetime.date.today(),"now your available balance is",self.balance)
        else:
            print("Transaction failed!")
    def balanc(self):
        print("Your",self.bank_name, "available balance is",self.balance)
obj=Bank()
obj.create_bank(556765552,"Sarath",998776762,500000,"Union bank")
obj.deposit_bank(30000)
# obj.withdraw_bank(100000)
obj.balanc()
