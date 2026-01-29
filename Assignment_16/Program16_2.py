def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
    
def main():
    print("Enter the Number : ",end="")
    Value=int(input())
    ChkNum(Value)

if __name__=="__main__":
    main()