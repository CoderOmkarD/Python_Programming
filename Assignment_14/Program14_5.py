
CheckEven=lambda a : a % 2 ==0 

def main():
    
    print("Enter the Number :")
    Value=int(input())

    
    Ret=CheckEven(Value)
    
    if Ret==True:
        print(Value,"is Even")
    else:
        print(Value ,"is Odd")
    
if __name__=="__main__":
    main()