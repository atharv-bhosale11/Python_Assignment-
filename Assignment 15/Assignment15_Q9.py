from functools import reduce
product = lambda a,b: a*b
    
def main():
    Data = [12,34,67,3,8,96,45,11,98,75,60,90,30]
    print("Actual Data is: ",Data)

    RData = reduce(product,Data)
    print("Product of all number are:  ",RData)

if __name__ == "__main__":
    main()
