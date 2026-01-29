def ChkDivisibeByFive(No):
    if No % 5 == 0:
        return True
    else :
        return False  
        
    
def main():
    
    print("Enter the Number : ")
    Value=int(input())    
    
    Ret=ChkDivisibeByFive(Value)
    
    print(Ret)
        
    
if __name__=="__main__":
    main()