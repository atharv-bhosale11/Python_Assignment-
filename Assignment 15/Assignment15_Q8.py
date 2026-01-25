divisible = lambda a: (a%3==0 and a%5==0) 
    
def main():
    Data = [12,34,67,3,8,96,45,11,98,75,60,90,30]
    print("Actual Data is: ",Data)

    RData = list(filter(divisible,Data))
    print("Divisible by 3 and 5 are: ",RData)

if __name__ == "__main__":
    main()
