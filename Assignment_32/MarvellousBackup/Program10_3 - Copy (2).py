def Factorial(no):
    Fact=1
    for i in range(1,no+1):
        Fact=Fact*i
    return Fact

def main():
    print("Enter the number")
    Value=int(input())
    Ret=Factorial(Value)
    print(f"Factorial is: {Ret}")
    
if __name__=="__main__":
    main()