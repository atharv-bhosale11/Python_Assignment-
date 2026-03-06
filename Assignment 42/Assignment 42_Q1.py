# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]

def SimpleLinearRegression():
    Border = "-"*95

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print(Border)
    print("Values of Independent Variables: X - ",X)
    print("Values of Independent Variables: Y - ",Y)

    print(Border)

    # Mean of X (X_bar)
    for i in X:
        meanX = sum(X)/len(X)
    print("Mean of x̄: ",meanX)

    # Mean of Y (Y_bar)
    for i in Y:
        meanY = sum(Y)/len(Y)
    print("Mean of Ȳ: ",meanY)

    print(Border)

    # X - X_bar and Summation
    # Y - Y_bar and Summation

    deviationX = [i - meanX for i in X]
    deviationY = [i - meanY for i in Y]

    print("X - X_bar: ",deviationX)
    print("Y - Y_bar: ",deviationY)
    print(Border)

    # (X - X_bar) * (Y - Y_bar)
    products_deviations = []
    for X_i, Y_i in zip(X,Y):
        deviationX = X_i - meanX
        deviationY = Y_i - meanY
        product = deviationX * deviationY
        products_deviations.append(product)

    print("Prodcut of Deviation:",products_deviations)

    sum_product = sum(products_deviations)

    print("Sum of(X - X_bar) * (Y - Y_bar): ",sum_product)
    print(Border)

    # (X - X_bar)**2
    squX = 0
    for i in X:
        square = (i - meanX) ** 2
        squX =  squX + square
    print("Sum of (X - X_bar)**2: ",squX)

    # (Y - Y_bar)**2
    squY = 0
    for i in Y:
        square = (i - meanY) ** 2
        squY  = squY + square
    print("Sum of (Y - Y_bar)**2: ",squY)
    print(Border)

    # Slope(m)
    slope = sum_product / squX
    print("Slope is: ",slope)
    print(Border)

    # Intercept Value(C)
    
    C = -(slope) * meanX + meanY
    print("Intercept value is: ",C)
    print(Border)

def main():
    SimpleLinearRegression()

if __name__ == "__main__":
    main()
