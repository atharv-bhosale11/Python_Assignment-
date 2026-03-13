import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def Exam():
    Border = "-"*50
    #load the data
    StudyHours = np.array([1,2,3,4,5]).reshape(-1,1)
    Marks = np.array([50,55,60,65,70])

    print(Border)
    print("Values of Independent Variables: X - ",StudyHours)
    print("Values of Dependent Variables: Y - ",Marks)

    model = LinearRegression()
    model.fit(StudyHours,Marks)

    print("Coefficient: ",model.coef_)  #Coefficient Value
    print("Intercept: ",model.intercept_)   #Intercept Value

def main():
    Exam()

if __name__ =="__main__":
    main()
