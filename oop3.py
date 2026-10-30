# classes
# customer - names, emails,kra pin dob, gender
# bank account -customer, acc_no,acc_type, balance

class Customer:
    def __init__(self, names:str,email:str, kra:str, dob:str, gender:str):
        self.names = names
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender
    def  show_details(self):
        print(f"name : {self.names}and KRA PIN:{self.kra}")
        #return f"Name : {self.names}and KRA PIN:{self.kra}"

class Account:
    def __init__(self, owner:Customer, acc_no:str, acc_type:str,balance:float):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("****************")
    def deposit(self,amount:float):
        self.balance += abs(amount)

    def withdraw(self,amount:float):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= abs(amount)
    def __str__(self) -> str:
        return f"{self.owner.names}{self.acc_no}{self.acc_type}{self.balance}"

owner1 = Customer(names= "jim jong", email="jj@test.com", kra="KRa001",dob="1980-01-01", gender="M")
owner2 = Customer(names="yaung Ti", email="yt@test.com", kra="KRa055",dob="1996-07-01", gender="M")

acc1 = Account(owner1, acc_no="98765", acc_type="current",balance=80_000)
acc2 = Account(owner1, acc_no="98766", acc_type="savings",balance=1_800_000)
acc3 = Account(owner1, acc_no="98767", acc_type="savings",balance=71_000)

#print(owner1.dob)# private
#print(owner1.show_details())

acc1.print_details()
acc1.deposit(-9000)
acc1.print_details()
acc1.withdraw(1_000)
acc1.print_details()

print(acc1.owner.)
print(acc1.acc_no)
