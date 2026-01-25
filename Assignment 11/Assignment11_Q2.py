def digit(N):
    cnt = 0
    while N>0:
        N = N//10
        cnt = cnt + 1
    return cnt

def main():
    N1 = int(input("Enter Number: "))
    Result = digit(N1)
    print("Digits are: ",Result)

if __name__ == "__main__":
    main()
