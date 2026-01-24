
def ChkNum(A):
    if A%2==0:
        print("Even Number")
    else:
        print("Odd Number")
    return A

def main():
    No = int(input("Enter the No: "))
    Ret = ChkNum(No)

if __name__=="__main__":
    main()
