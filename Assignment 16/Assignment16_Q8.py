
def display(A):
    for i in range(A):
        print("*",end=" ")

def main():
    No = int(input("How many stars you want: "))
    Ret = display(No)

if __name__=="__main__":
    main()
