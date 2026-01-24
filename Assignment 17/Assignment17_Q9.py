def count(A):
    
    return len(str(A))

def main():
    No = int(input("Enter the Number: "))
    Ret = count(No)
    print("Counts are: ",Ret)


if __name__=="__main__":
    main()
