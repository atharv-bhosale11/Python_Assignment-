from functools import reduce

add = lambda a,b: a+b

def main():
    Data = [12,45,67,3,8,96,45,11,98]
    print("Actual Data is: ",Data)

    RData = reduce(add,Data)
    print("Additon is: ",RData)

if __name__ == "__main__":
    main()
