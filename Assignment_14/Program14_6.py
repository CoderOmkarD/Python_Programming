
CheckOdd=lambda a : a % 2 !=0 

def main():
    
    print("Enter the Number :")
    Value=int(input())

    
    Ret=CheckOdd(Value)
    
    if Ret==True:
        print(Value,"is Odd")
    else:
        print(Value ,"is Even")
    
if __name__=="__main__":
    main()