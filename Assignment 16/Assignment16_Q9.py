
def even(A):
    for i in range(2,A+1):
        if i%2==0:
            print(i)
    return A

def main():
    No = int(input("Enter first number: "))
    Ret = even(No)

if __name__=="__main__":
    main()
