from functools import reduce

def Prime(data):
    if data <= 1:
        return False
    for i in range(2, int(data ** 0.5) + 1):
        if data % i == 0:
            return False
    return True

def Mul(N):
    return N*2

def Max(a,b):
    if a>b:
        return a
    else:
        return b

def main():
    No=int(input("How many numbers you want to add: "))
    data=[]
    for i in range(No):
        i = int(input("Enter all Numbers: "))
        data.append(i)
    print("Your data is: ",data)

    FData = list(filter(Prime,data))
    print("Your Prime Numbers Data is:  ",FData)

    MData=list(map(Mul,FData))
    print("Your data after Multiply by 2 ",MData)

    RData=reduce(Max,MData)
    print("Maximum number is ",RData)

if __name__=="__main__":
    main()
