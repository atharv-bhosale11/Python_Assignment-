def AddEle(A):
    Ans = 0
    for i in range(A):
        Num = int(input("Enter all numbers: "))
        Ans = Ans + Num
    return Ans

def main():
    Num = int(input("Enter the Numbers you want to print: "))    
    Ret = AddEle(Num)
    print("Addition is: ",Ret)

if __name__=="__main__":
    main()
