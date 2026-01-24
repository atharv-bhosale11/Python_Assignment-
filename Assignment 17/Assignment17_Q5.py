def Prime(No):
    if No%2==0:
        print("Not a prime number")
    else:
        print("Prime Number")
    return No

def main():
    A = int(input("Enter Number: "))
    Ret = Prime(A)

if __name__=="__main__":
    main()
