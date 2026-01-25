def Circle(r):
    c = 3.13*(r*r)
    return c

def main():
    num1 = int(input("Enter Radius: "))
    Ret = Circle(num1)
    print("Area of Circle : ",Ret)

if __name__ == "__main__":
    main()
