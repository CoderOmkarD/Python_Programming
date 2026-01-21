def SumOfDigits(no):
    Digit=0
    Sum=0
    while(no!=0):
        Digit=int(no%10)
        
        Sum=Sum+Digit
        
        no=int(no/10)
    return Sum
   
   

def main():
    print("Enter the number")
    Value=int(input())
    
    Ret=SumOfDigits(Value)
    
    print("Summation of digits is: ",Ret)
   

if __name__=="__main__":
    main()