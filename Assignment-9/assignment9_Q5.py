def divisibility(c):
    if c%3==0 and c%5==0:
        print("The Number is divisible by 5 and 3")
    else:
        print("The Number is not divisible by 5 and 3")
    return c

def main():
    No = int(input("Enter the number: "))
    Result = divisibility(No)
    
if __name__ == "__main__":
    main()
