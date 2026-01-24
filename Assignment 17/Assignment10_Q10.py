def Sum(n):
    total = 0
    while n > 0:
        total = total + n % 10
        n //= 10
    return total

def main():
    num = int(input("Enter number: "))
    print("Sum of digits:", Sum(num))

if __name__ == "__main__":
    main()
