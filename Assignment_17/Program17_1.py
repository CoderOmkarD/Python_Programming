from Arithmetic import *


def main():

    print("Enter two number : ")
    Value1 = int(input())
    Value2 = int(input())

    Ret = Addition(Value1, Value2)
    print("Addition is : ", Ret)

    Ret = Subtraction(Value1, Value2)
    print("Subtraction is : ", Ret)

    Ret = Division(Value1, Value2)
    print("Division is : ", Ret)

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is : ", Ret)


if __name__ == "__main__":
    main()
