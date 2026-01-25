maximum = lambda Num1,Num2 : Num1 if Num1>Num2 else Num2

def main():         
    No1 = int(input("Enter the number: "))
    No2 = int(input("Enter Second Number: "))
    Ret= maximum(No1,No2)
    print(Ret,"is greater number")

if (__name__=="__main__"):
    main()
