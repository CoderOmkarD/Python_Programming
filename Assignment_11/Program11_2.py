
def CountDigits(no):
    iCount=0
    while(no!=0):
        iCount=iCount+1
        no=int(no/10)
    return iCount 
   
   

def main():
    print("Enter the number")
    Value=int(input())
    
    Ret=CountDigits(Value)
    
    print("No. of digis is: ",Ret)
   

if __name__=="__main__":
    main()