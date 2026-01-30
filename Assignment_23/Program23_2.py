class BankAccount:

    ROI=10.5

    def __init__(self,AccountHolderName,AccountBal):

        self.Name=AccountHolderName
        self.Amount=AccountBal

    def Display(self):
        print("Account Holder Name :",self.Name)
        print("Account Balance:",self.Amount)

    def Deposit(self,NewAmount):
        self.Amount=self.Amount+NewAmount

    def Withdraw(self,NewAmount):
        if self.Amount >= NewAmount:
            self.Amount=self.Amount-NewAmount
        else:
            print("Insufficient Balance")
    
    def CalculateInterest(self):
        Interest=(self.Amount * BankAccount.ROI)/100
        return Interest

def main():

    obj1=BankAccount("Omkar Durge",1000)
    obj1.Display()
    obj1.Deposit(500)
    obj1.Withdraw(10000)

    obj1.Display()
    Ret=obj1.CalculateInterest()
    print("Interest :",Ret)

  

if __name__ == "__main__":
    main()
