
isDivisibeByFive=lambda a : a % 5 ==0 

def main():
    
    print("Enter the Number :")
    Value=int(input())

    
    Ret=isDivisibeByFive(Value)
    
    if Ret==True:
        print(Value,"is Divisible by 5")
    else:
        print(Value ,"is not Divisile by 5")
    
if __name__=="__main__":
    main()