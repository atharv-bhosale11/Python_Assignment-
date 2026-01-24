
def ChkNum(A):
    if(A%5==0):
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")
    return A

def main():
    No = int(input("Enter the Number: "))
    Result = ChkNum(No)

if __name__=="__main__":
    main()
