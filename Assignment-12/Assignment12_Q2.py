def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
    return n
    
def main():
    N = int(input("Enter Number: "))
    Result = factor(N)

if __name__ == "__main__":
    main()
