def SumOfNaturalNum(no):
    Sum=0
    for i in range(1,no+1):
        Sum=Sum+i
    return Sum

def main():
    print("Enter the number")
    Value=int(input())
    Ret=SumOfNaturalNum(Value)
    print(f"Sum is: {Ret}")
    
if __name__=="__main__":
    main()