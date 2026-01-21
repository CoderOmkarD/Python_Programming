def CheckPrime(no):
    
    for i in range(2,int(no+1/2)):
        
        if no%i==0:
            return False
    return True
   

def main():
    print("Enter the number")
    Value=int(input())
    Ret=CheckPrime(Value)
    
    if Ret==True:
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__=="__main__":
    main()