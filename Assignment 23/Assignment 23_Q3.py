class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

def main():
    n = int(input("How many numbers do you want to check? "))
    for i in range(n):
        num = int(input("Enter a number: "))
        obj = Numbers(num)

        print("Number:", obj.Value)
        print("Prime:", obj.ChkPrime())
        print("Perfect:", obj.ChkPerfect())
        obj.Factors()
        print("Sum of factors:", obj.SumFactors())


if __name__ == "__main__":
    main()
