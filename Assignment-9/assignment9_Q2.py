def ChkGreater(N1,N2):
    if N1>N2:
        return N1
    else:
        return N2
    
def main():
    N1 = int(input("Enter first number: "))
    N2 = int(input("Enter second Number: "))
    Result = ChkGreater(N1,N2)
    print("Greater Number is: ",Result)

if __name__ == "__main__":
    main()
