class Atm_account:
    def __init__(self):
        self.balance=200
        print("Hello!!! Welcome to the ATM")
 
    def deposit(self):
        amount1=int(input("Enter amount to be Deposited: "))
        self.balance =self.balance+amount1
        print("\n New amount:",self.balance)
        print("\n Amount Deposited:",amount1)
 
    def withdraw(self):
        amount2 = int(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount2:
            self.balance=self.balance-amount2
            print("\n You Withdrew:", amount2)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 

  

a = Atm_account()
  

a.deposit()
a.withdraw()
a.display()