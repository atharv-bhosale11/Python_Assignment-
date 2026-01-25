def Min(A):
    Ans = None
    for i in range(A):
        No = int(input("Enter the Numbers: "))
        if Ans is None or No<Ans:
            Ans = No
    return Ans

def main():
    Num = int(input("Enter the Number you want to Print: "))
    Ret = Min(Num)
    print("Minimum Number is: ",Ret)

if __name__=="__main__":
    main()
