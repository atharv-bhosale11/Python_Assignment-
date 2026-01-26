import threading

def EvenList(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers:", even_numbers)
    print("Sum of even numbers:", sum(even_numbers))

def OddList(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print("Odd numbers:", odd_numbers)
    print("Sum of odd numbers:", sum(odd_numbers))

def main():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    # Create threads
    t1 = threading.Thread(target=EvenList, args=(numbers,))
    t2 = threading.Thread(target=OddList, args=(numbers,))

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    print("Processing completed.")

if __name__ == "__main__":
    main()
