def even(N):
    for i in range(0,N+1):
        if i%2==0:
            print(i)
    return N

def main():
    N1 = int(input("Enter Number: "))
    Result = even(N1)
    print("All even number: ",Result)

if __name__ == "__main__":
    main()
