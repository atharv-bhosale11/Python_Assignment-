import threading

def EvenFactor(n):
    even_factors = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            even_factors.append(i)
    print("Even factors of {n}: {even_factors}")
    print("Sum of even factors: {sum(even_factors)}")

def OddFactor(n):
    odd_factors = []
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            odd_factors.append(i)
    print(f"Odd factors of {n}: {odd_factors}")
    print(f"Sum of odd factors: {sum(odd_factors)}\n")

def main():
    number = int(input("Enter a number: "))

    t1 = threading.Thread(target=EvenFactor, args=(number,), name="EvenFactor")
    t2 = threading.Thread(target=OddFactor, args=(number,), name="OddFactor")

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to complete
    t1.join()
    t2.join()

    # Main thread message
    print("Exit from main")

if __name__ == "__main__":
    main()
