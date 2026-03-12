import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def Exam():
    Border = "-"*50
    #load the data
    StudyHours = [1,2,3,4,5]
    SleepHours = [7,6,7,6,8]
    Marks = [50,55,60,65,70]

    print(Border)

    X = np.array(list(zip(StudyHours,SleepHours)))
    Y = np.array(Marks)

    print("Values of Independent Variables: X - ",X)
    print("Values of Independent Variables: Y - ",Y)

    model = LinearRegression()
    model.fit(X,Y)

    print("Coefficient for StudyHours: ",model.coef_[0])  #Coefficient Value of StudyHours
    print("Coefficient for SleepHours: ",model.coef_[1])  #Coefficient Value of SleepHours

    print("Intercept: ",model.intercept_)   #Intercept Value

def main():
    Exam()

if __name__ =="__main__":
    main()
