
def SD():
    Border = "-"*60

    data = [4,6,8,10,12]

    mean = sum(data) / len(data)
    print("Mean is: ",mean)  # Mean 
    print(Border)

    deviations = []

    for i in data:
        deviation = i - mean
        deviations.append(deviation)

    print("Deviations: ",deviations)  #Deviation = Xi - X_bar
    print(Border)

    squares = []

    for i in deviations:
        square = i*i
        squares.append(square)
    print("Deviation of each square: ",squares)  #Square of Deviation
    print(Border)

    add = 0
    for i in squares:
        add = add + i
    print("(Sum of Xi - X_bar)**2: ",add)
    print(Border)
   
    variance = add / len(data)
    print("Variance : ",variance)  #Variance
    print(Border)

def main():
    SD()

if __name__ =="__main__":
    main()
