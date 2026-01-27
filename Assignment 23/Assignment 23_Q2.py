class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name= Name
        self.Amount=Amount

    def Display(self):
        print("Account Holder Name:",self.Name)
        print("Current Balance is: ",self.Amount)

    def Deposit(self):
        Amt = float(input("Enter the Deposit amount: "))
        self.Amount = self.Amount+Amt
        print("Amount deposit successfully!!!")
    
    def Withdraw(self):
        Wid = float(input("Enter the Withdrawl Amount: "))
        
        if Wid<=self.Amount:
            print("Amount withdrawl succesful")
        else:
            print("Insufficient Balance!!")
    
    def CalculateInterest(self):
        Interst = (self.Amount*BankAccount.ROI)/100
        print("Interst is: ",Interst)
    
obj1 =BankAccount("Atharv",20000)
obj2 =BankAccount("Bhosale",15000)

obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
print("-----------------------------------------------------")
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()
