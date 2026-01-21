def Area(Length,Width):
    Ans=Length*Width
    return Ans

def main():
    print("Enter the Width:")
    Value1=int(input())
    print("Enter the Length:")
    Value2=int(input())
    Ret=Area(Value1,Value2)
    print("Area of Reactangle is :",Ret)

if __name__=="__main__":
    main()