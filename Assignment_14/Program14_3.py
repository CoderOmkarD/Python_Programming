
Max=lambda a, b : a > b 

def main():
    
    print("Enter two Number :")
    Value1=int(input())
    Value2=int(input())
    
    Ret=Max(Value1,Value2)
    
    if Ret==True:
        print(Value1," is Maximum")
    else:
        print(Value2 ,"is MAximum")
    
if __name__=="__main__":
    main()