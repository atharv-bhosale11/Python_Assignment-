def Square(c):
    c = c*c*c
    return c

def main():
    No = int(input("Enter the number: "))
    Result = Square(No)
    print("The Square is: ",Result)
    
if __name__ == "__main__":
    main()
