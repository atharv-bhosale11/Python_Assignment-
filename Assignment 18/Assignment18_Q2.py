def max(A):
    Ans = None
    for i in range(A):
        No = int(input("Enter all numbers: "))
    if Ans is None or No>Ans:
        Ans=No
    return  Ans

def main():
    Num = int(input("Enter the Number: "))
    Ret = max(Num)
    print("Maximum Number is: ",Ret)

if __name__=="__main__":
    main()
