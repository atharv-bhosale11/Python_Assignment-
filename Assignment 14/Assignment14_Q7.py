checkdivisibility = lambda Num1 : Num1%5==0

def main():
    No1 = int(input("Enter the Number: "))
    Ret = checkdivisibility(No1)

    if Ret:
        print(No1,"is divisible by 5")
    else:
        print(No1,"is not divisible by 5")

if __name__=="__main__":
    main()
