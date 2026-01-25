checkEven = lambda Num1: Num1%2==0

def main():
    No1=int(input("Enter First Number: "))
    Ret = checkEven(No1)
    
    if Ret:
        print(No1,"is even Number")
    else:
        print(No1,"is odd Number")

if __name__ == "__main__":
    main()
