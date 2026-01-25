minimum = lambda Num1,Num2 : Num1 if Num1<Num2 else Num2

def main():
    No1=int(input("Enter First Number: "))
    No2=int(input("Enter Second Number: "))
    Ret = minimum(No1,No2)
    print(Ret,"is minimum number")

if __name__ == "__main__":
    main()
