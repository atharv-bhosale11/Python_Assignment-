def binary(N):
    binary = ""
    if N==0:
        binary="0"

    while N>0:
        rem = N%2
        binary=str(rem)+binary
        N=N//2
    return binary
    
def main():
    num1 = int(input("Enter Number: "))
    Ret = binary(num1)
    print(Ret)

if __name__ == "__main__":
    main()
