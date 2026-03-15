import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix


###################################################################
# Function Name:        DisplayInfo
# Description:          Displays formatted title
# Parameters:           title (str)
# Return:               None
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def DisplayInfo(title):

    print("\n" + "="*75)
    print(title)
    print("="*75)


###################################################################
# Function Name:        LoadDataset
# Description:          Loads dataset from CSV file
# Parameters:           Datapath (str)
# Return:               df -> Pandas DataFrame
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def LoadDataset(Datapath):

    DisplayInfo("Step 1 : Load Dataset")

    df = pd.read_csv(Datapath)

    print("First Five Records")
    print(df.head())

    print("\nLast Five Records")
    print(df.tail())

    print("\nShape of Dataset:",df.shape)

    return df


###################################################################
# Function Name:        CleanDataset
# Description:          Removes unwanted columns and checks missing values
# Parameters:           df -> Pandas DataFrame
# Return:               df -> Clean Pandas DataFrame
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def CleanDataset(df):

    DisplayInfo("Step 2 : Clean Dataset")

    print("Shape before cleaning:",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape after cleaning:",df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    return df


###################################################################
# Function Name:        DatasetStatistics
# Description:          Displays statistical summary and correlation
# Parameters:           df -> Pandas DataFrame
# Return:               None
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def DatasetStatistics(df):

    DisplayInfo("Step 3 : Dataset Statistics")

    print("\nStatistical Summary")
    print(df.describe())

    print("\nCorrelation Matrix")
    print(df.corr())


###################################################################
# Function Name:        ShowConfusionMatrix
# Description:          Displays confusion matrix using heatmap
# Parameters:           Y_test -> Actual values
#                       Y_pred -> Predicted values
# Return:               None
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def ShowConfusionMatrix(Y_test,Y_pred):

    DisplayInfo("Step 11 : Confusion Matrix (Visual)")

    threshold = Y_test.median()

    Y_test_class = (Y_test > threshold).astype(int)
    Y_pred_class = (Y_pred > threshold).astype(int)

    cm = confusion_matrix(Y_test_class,Y_pred_class)

    print("Confusion Matrix:")
    print(cm)

    plt.figure(figsize=(6,4))
    sns.heatmap(cm,annot=True,fmt="d",cmap="Blues")

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")

    plt.show()


###################################################################
# Function Name:        ShowGraphs
# Description:          Displays actual vs predicted graph
# Parameters:           Y_test -> Actual values
#                       Y_pred -> Predicted values
# Return:               None
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def ShowGraphs(Y_test,Y_pred):

    DisplayInfo("Step 12 : Actual vs Predicted Graph")

    plt.figure(figsize=(8,5))

    plt.scatter(Y_test,Y_pred)

    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")

    plt.title("Actual Sales vs Predicted Sales")

    plt.grid(True)

    plt.show()


###################################################################
# Function Name:        TrainAdvertiseModel
# Description:          Train Linear Regression Model and evaluate
# Parameters:           df -> Pandas DataFrame
# Return:               None
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def TrainAdvertiseModel(df):

    DisplayInfo("Step 4 : Split Independent and Dependent Variables")

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape)


    DisplayInfo("Step 5 : Train Test Split")

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,Y,test_size=0.2,random_state=42)

    print("X_train:",X_train.shape)
    print("X_test:",X_test.shape)
    print("Y_train:",Y_train.shape)
    print("Y_test:",Y_test.shape)


    DisplayInfo("Step 6 : Train Linear Regression Model")

    model = LinearRegression()

    model.fit(X_train,Y_train)

    print("Model trained successfully")


    DisplayInfo("Step 7 : Prediction")

    Y_pred = model.predict(X_test)


    DisplayInfo("Step 8 : Model Evaluation")

    mse = mean_squared_error(Y_test,Y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error :",mse)
    print("Root Mean Squared Error :",rmse)
    print("R2 Score :",r2)


    DisplayInfo("Step 9 : Model Coefficients")

    for column,value in zip(X.columns,model.coef_):
        print(column," : ",value)

    print("Intercept :",model.intercept_)


    DisplayInfo("Step 10 : Actual vs Predicted Table")

    result = pd.DataFrame({
        "Actual Sales":Y_test.values,
        "Predicted Sales":Y_pred
    })

    print(result.head())


    ShowConfusionMatrix(Y_test,Y_pred)

    ShowGraphs(Y_test,Y_pred)


###################################################################
# Function Name:        MarvellousAdvertise
# Description:          Main pipeline controller
# Parameters:           Datapath (str)
# Return:               None
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def MarvellousAdvertise(Datapath):

    df = LoadDataset(Datapath)

    df = CleanDataset(df)

    DatasetStatistics(df)

    TrainAdvertiseModel(df)


###################################################################
# Function Name:        main
# Description:          Entry point of application
# Parameters:           None
# Return:               None
# Date:                 15/03/2026
# Author:               Atharv Tushar Bhosale
###################################################################

def main():

    MarvellousAdvertise("Advertising.csv")


if __name__ == "__main__":
    main()
