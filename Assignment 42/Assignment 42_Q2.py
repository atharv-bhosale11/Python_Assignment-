# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]

def MSE(actual_value,pred_value):
    if len(actual_value)!= len(pred_value):
        raise ValueError("Actual and Predicted values lists must have the same length")
    
    n = len(actual_value)
    total_square_error = 0

    for i in range(n):
        error = actual_value[i] - pred_value[i]
        total_square_error += error ** 2

    mse = total_square_error / n
    return mse

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

    # Predicting Values of Y equation 

    for i in X:
        y_pred = (slope * i) + C
        print("For X = ",i,"Predicted Y",y_pred)
    print(Border)

    # MSE
    predicted_values = []

    for i in X:
        y_pred = (slope * i) + C
        predicted_values.append(y_pred)
        print("For X =",i,"Predicted Y =",y_pred)

    mse_value = MSE(Y, predicted_values)    # call the function
    print(Border)
    print("Mean Squared Error:", mse_value)
    print(Border)

    sum_value = 0

    # Y_pred  - Y_bar
    for i in predicted_values:
        value = i - meanY      
        sum_value = sum_value + value
        print("Y_pred - Y_bar =", value)

    print("Summation of Y_pred - Y_bar =",sum_value)
    print(Border)

    # (Y_pred - Y_bar) ** 2
    for i in predicted_values:
        value = (i - meanY) **2      
        sum_value = sum_value + value
        print("(Y_pred - Y_bar)**2 =", value)

    print("(Summation of Y_pred - Y_bar)**2 =",sum_value)
    print(Border)

    # R_square
    R_square = sum_value / squY

    print("R_suare is: ",R_square)
    print(Border)

def main():

    SimpleLinearRegression()

if __name__ == "__main__":
    main()
