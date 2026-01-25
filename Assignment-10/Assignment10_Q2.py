def sum(a):
    Ans = 0
    for i in range(1,a+1):
        Ans = Ans + i
    return Ans

def main():
    Num = int(input("Enter the number: "))
    Result = sum(Num)
    print("Sum of Number is: ",Result)

if __name__ == "__main__":
    main()
