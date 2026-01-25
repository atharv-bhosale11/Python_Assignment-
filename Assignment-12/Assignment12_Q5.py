def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    print("Reversed number is:", rev)

def main():
    num = int(input("Enter number: "))
    reverse_number(num)

if __name__ == "__main__":
    main()
