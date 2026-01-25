def sumdigit(N):
    Ans = 0
    while N>0:
        digit = N%10
        Ans = Ans + digit
        N = N//10
    return Ans

def main():
    N1 = int(input("Enter Number: "))
    Result = sumdigit(N1)
    print("Sum of Digits are: ",Result)

if __name__ == "__main__":
    main()
