import threading

def max(num):
    print("Maximum element:", max(num))

def min(num):
    print("Minimum element:", min(num))

def main():
    nums = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=max, args=(nums,))
    t2 = threading.Thread(target=min, args=(nums,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
