import math

def SD():
    Border = "-"*60

    data = [5,7,9,11,13]    #Load the Data

    mean = sum(data) / len(data)    #Mean
    print("Mean is: ",mean) 
    print(Border)

    deviations = []

    for i in data:
        deviation = i - mean    #Deviation = Xi - X_bar
        deviations.append(deviation)

    print("Deviations: ",deviations)
    print(Border)

    squares = []

    for i in deviations:
        square = i*i    #Square of Each Deviation
        squares.append(square)
    print("Deviation of each square: ",squares)
    print(Border)

    add = 0
    for i in squares:
        add = add + i   #Summation
    print("(Sum of Xi - X_bar)**2: ",add)
    print(Border)
   
    variance = add / len(data)  #Variance
    print("Variance : ",variance)
    print(Border)

    StandardDeviation = math.sqrt(variance) #Standard Deviation
    print("Standard Deviation: ",StandardDeviation)
    print(Border)

def main():
    SD()

if __name__ =="__main__":
    main()
