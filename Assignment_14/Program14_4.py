
Min=lambda a, b : a < b 

def main():
    
    print("Enter two Number :")
    Value1=int(input())
    Value2=int(input())
    
    Ret=Min(Value1,Value2)
    
    if Ret==True:
        print(Value1,"is Minimum")
    else:
        print(Value2 ,"is Minimum")
    
if __name__=="__main__":
    main()