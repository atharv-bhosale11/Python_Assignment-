def factors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total


def main():
    num = int(input("Enter a number: "))
    result = factors(num)
    print("Sum of factors is:", result)

if __name__ == "__main__":
    main()
