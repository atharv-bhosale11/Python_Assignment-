from functools import reduce

def Gretaer70(data):
    if data >=70:
        return data
    
def Increment(N):
    return N +10

def Product(a,b):
    return a*b

def main():
    No=int(input("How many numbers you want to add: "))
    data=[]
    for i in range(No):
        i = int(input("Enter all Numbers: "))
        data.append(i)
    print("Your data is: ",data)

    FData = list(filter(Gretaer70,data))
    print("Your data which is greater than 70 is: ",FData)

    MData=list(map(Increment,FData))
    print("Your Data after increment by 10: ",MData)

    RData=reduce(Product,MData)
    print("Product of all data is: ",RData)

if __name__=="__main__":
    main()
