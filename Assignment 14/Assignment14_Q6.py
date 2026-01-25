checkOdd = lambda Num1 : Num1%2!=0

def main():
    No1 = int(input("Enter the Number: "))
    Ret = checkOdd(No1)

    if Ret:
        print(No1,"is odd number")
    else:
        print(No1,"is even number")

if __name__=="__main__":
    main()
