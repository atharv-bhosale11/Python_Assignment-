def Freq(arr,search):
    Cnt = 0
    for No in arr:
        if No==search:
            Cnt+=1
    return Cnt
def main():
    No = int(input("Enter the Number want to take from user: "))
    arr =[]

    for i in range(No):
        arr.append(int(input("Enter all Numbers: ")))

    search = int(input("Enter the elemnts want to search: "))
    Ret = Freq(arr,search)
    print("Your frequncy is: ",Ret)

if __name__=="__main__":
    main()
