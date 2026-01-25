def perfectnum(N):
    Ans = 0
    for i in range(1,N):
        if N%i==0:
            Ans = Ans + i
    if Ans == N:
        print("Perfect Number")
    else:
        print("Not perfect Number")
    

def main():
    num1 = int(input("Enter Number: "))
    Ret = perfectnum(num1)

if __name__ == "__main__":
    main()
