def CheckPalindrome(no):
    temp=no
    
    Digit=0
    Rev=0
    while(no!=0):
        
        Digit=int(no%10)
        
        Rev=int(Rev*10)+Digit
        
        no=int(no/10)
    
    
    
    if temp==Rev:
        return True
    else:
        return False
   
   

def main():
    
    print("Enter the number")
    Value=int(input())
    
    Ret=CheckPalindrome(Value)
    
    if Ret==True:
        print("It is a palindrome number")
    else:
        print("It is not a palindrome number")

if __name__=="__main__":
    main()