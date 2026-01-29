
Maximum=lambda a , b , c: a if a>=b and a>=c else (b if b>=c and b>=c else c)

def main():
    
    print("Enter three Number :")
    Value1=int(input())
    Value2=int(input())
    Value3=int(input())

    
    Ret=Maximum(Value1,Value2,Value3)
    
    print("Maximum is :",Ret)
if __name__=="__main__":
    main()