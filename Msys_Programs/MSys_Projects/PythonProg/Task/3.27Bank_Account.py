class Bank_Account:
    bank_name = 'ICICI'
    branch = 'Banglore'
    ifsc_code = 'ICICI123'

    def __init__(self,acc_name,acc_no,ifsc,balance):
        self.Acc_Name = acc_name
        self.Acc_No = acc_no
        self.IFSC = ifsc
        self.Balance = balance

    def account_details(self):
        pass

    def __str__(self):
        return f''' ==== Account Details =======
        Bank Name: {self.bank_name}
        branch: {self.branch}
        ifsc: {self.ifsc_code}'''
   
    def deposit(self,amount):
        self.Balance += amount
        print(f"the amount of {amount} is deposited successfully.current balance is {self.Balance}")

    def withdraw(self,amount):
        if amount > self.Balance:
            print("the amount is insufficient")
        else:
            self.Balance -= amount
            print(f'withdrawal of {amount} is successful and current balance is {self.Balance}')

    def get_balance(self):
        return self.Balance

depo = int(input("Enter deposit amount: "))
withd = int(input("Enter withdraw amount: "))
a = Bank_Account('Vishal',123456789,'icici001',5000)
print(a.Acc_Name)
a.deposit(depo)
a.withdraw(withd)
print(a.get_balance())
print(a)