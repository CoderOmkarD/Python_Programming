class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter two Numbers :")
        self.Value1 = int(input())
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError as zobj:
            print("Please enter non zero number ")


def main():

    aobj1 = Arithmetic()
    aobj1.Accept()

    Ans = aobj1.Addition()
    print("Addition is :", Ans)

    Ans = aobj1.Substraction()
    print("Substraction is :", Ans)

    Ans = aobj1.Multiplication()
    print("Multiplication is :", Ans)

    Ans = aobj1.Division()
    print("Division is :", Ans)

    aobj2 = Arithmetic()
    aobj2.Accept()

    Ans = aobj2.Addition()
    print("Addition is :", Ans)

    Ans = aobj2.Substraction()
    print("Substraction is :", Ans)

    Ans = aobj2.Multiplication()
    print("Multiplication is :", Ans)

    Ans = aobj2.Division()
    print("Division is :", Ans)


if __name__ == "__main__":
    main()
