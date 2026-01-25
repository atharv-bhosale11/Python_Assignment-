largest = lambda a,b,c: a if(a>b and a>c) else (b if b>c and b>a else c)

def main():
    No1=int(input("Enter the First Number: "))
    No2=int(input("Enter the Second Number: "))
    No3=int(input("Enter the Third Number: "))

    Ret = largest(No1,No2,No3)
    print("Largest Number is: ",Ret)

if __name__ == "__main__":
    main()
