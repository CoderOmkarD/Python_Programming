def Len(name):
    
    return len(name)
        
    
def main():
    
    print("Enter the Name : ")
    Value=str(input())    
    
    Ret=Len(Value)  
    
    print("Length is :",Ret)     
    
if __name__=="__main__":
    main()