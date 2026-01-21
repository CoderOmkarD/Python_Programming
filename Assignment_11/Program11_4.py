def Reverse(no):
    Digit=0
    
    Rev=0
    while(no!=0):
        
        Digit=int(no%10)
        
        Rev=int(Rev*10)+Digit
        
        no=int(no/10)
        
    return Rev
   
   

def main():
    
    print("Enter the number")
    Value=int(input())
    
    Ret=Reverse(Value)
    
    print("Reverse no. is: ",Ret)
   

if __name__=="__main__":
    main()