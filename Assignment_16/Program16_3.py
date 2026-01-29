def Add(No1,No2):
    Ans=No1+No2
    return Ans
    
def main():
    print("Enter two Number : ")
    
    Value1=int(input())
    Value2=int(input())
    
    Ret=Add(Value1,Value2)
    print("Addition is : ",Ret)

if __name__=="__main__":
    main()