class Numbers:
    def __init__(self, No):
        self.Value = No

    def ChkPrime(self):

        if self.Value < 2:
            return False

        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are:")
        for i in range(1, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False


def main():
    obj1 = Numbers(11)

    print("Is Prime :", obj1.ChkPrime())
    print("Is Perfect :", obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors :", obj1.SumFactors())

    print("------------------------")

    obj2 = Numbers(28)

    print("Is Prime :", obj2.ChkPrime())
    print("Is Perfect :", obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors :", obj2.SumFactors())


if __name__ == "__main__":
    main()
