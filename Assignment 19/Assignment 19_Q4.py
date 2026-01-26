from functools import reduce

def even(data):
    if data%2==0:
        return data
    
def Square(N):
    return N*N

def addition(a,b):
    return a+b

def main():
    No=int(input("How many numbers you want to add: "))
    data=[]
    for i in range(No):
        i = int(input("Enter all Numbers: "))
        data.append(i)
    print("Your data is: ",data)

    FData = list(filter(even,data))
    print("Your Even Data is:  ",FData)

    MData=list(map(Square,FData))
    print("Your Square of all Number is ",MData)

    RData=reduce(addition,MData)
    print("Addition of all data is: ",RData)

if __name__=="__main__":
    main()
