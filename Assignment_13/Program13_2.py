def AreaOfCircle(Radius):
    Area=3.1415*Radius*Radius
    return Area

def main():
    print("Enter the radius :")
    Value=int(input())
    Ret=AreaOfCircle(Value)
    print("Area of circle is :",Ret)

if __name__=="__main__":
    main()