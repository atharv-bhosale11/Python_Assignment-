
#Sum and Product Using Two Threads

import threading

sum_result = 0
product_result = 1

def sum(nums):
    global sum_result
    sum_result = sum(nums)

def product(nums):
    global product_result
    for n in nums:
        product_result *= n

def main():
    nums = list(map(int, input("Enter numbers: ").split()))

    t1 = threading.Thread(target=sum, args=(nums,))
    t2 = threading.Thread(target=product, args=(nums,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum =", sum_result)
    print("Product =", product_result)

if __name__ == "__main__":
    main()
