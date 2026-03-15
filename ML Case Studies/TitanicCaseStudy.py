import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

###################################################################
# Function Name : ShowGraphs
# Description   : Displays graphical representation of the dataset
#                 including survival count, age distribution and
#                 confusion matrix for model evaluation.
# Parameters    :
#       df      : Cleaned Titanic dataset (DataFrame)
#       Y_test  : Actual test labels
#       Y_pred  : Predicted labels from the trained model
# Returns       : None
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def ShowGraphs(df, Y_test, Y_pred):

    # Survival Count Graph
    plt.figure(figsize=(6,4))
    sns.countplot(x="Survived", data=df)
    plt.title("Survival Count")
    plt.xlabel("Survived (0 = No, 1 = Yes)")
    plt.ylabel("Number of Passengers")
    plt.show()

    # Age Distribution
    plt.figure(figsize=(6,4))
    sns.histplot(df["Age"], bins=20, kde=True)
    plt.title("Age Distribution of Passengers")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

    # Confusion Matrix Graph
    cm = confusion_matrix(Y_test, Y_pred)

    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

###################################################################
# Function Name : LoadPreserveModel
# Description   : Loads the previously saved machine learning model
#                 from secondary storage using joblib.
# Parameters    :
#       filename : Name of the saved model file (.pkl)
# Returns       : Loaded trained model
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def LoadPreserveModel(filename):
    loaded_model = joblib.load(filename)
    print("Model Succesfully Loaded!!!!!")
    return loaded_model

###################################################################
# Function Name : Preserve_model
# Description   : Saves the trained machine learning model to
#                 secondary storage using joblib.
# Parameters    :
#       model    : Trained machine learning model
#       filename : Name of the file where the model will be stored
# Returns       : None
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def Preserve_model(model,filename):
    joblib.dump(model,filename)

    print("Model Preserved Successfully with Name: ",filename)

###################################################################
# Function Name : TrainTitanicModel
# Description   : Splits the dataset into training and testing sets,
#                 trains the Logistic Regression model and evaluates
#                 the model using accuracy and confusion matrix.
# Parameters    :
#       df : Preprocessed Titanic dataset (DataFrame)
# Returns       : None
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def TrainTitanicModel(df):
    # Split features and labels
    X = df.drop("Survived", axis = 1) 
    Y = df["Survived"]

    print("\nFeatures: ")
    print(X.head())

    print("\nLabels: ")
    print(Y.head())

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    
    print("X_train Shape",X_train.shape)
    print("X_test Shape",X_test.shape)
    print("Y_train Shape",Y_train.shape)
    print("Y_test Shape",Y_test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train,Y_train)

    print("Model Trained Successfully!!!!!")

    print("Intercept of Model: ")
    print(model.intercept_)

    print("Coefficient of Model: ")
    for feature,coefficient in zip(X.columns,model.coef_[0]):
        print(feature, " : ",coefficient)

    Preserve_model(model,"Marvelloustitanic.pkl")

    loaded_model = LoadPreserveModel("Marvelloustitanic.pkl")

    Y_pred = loaded_model.predict(X_test)

    accuracy = accuracy_score(Y_pred,Y_test)

    print("Accuracy is: ",accuracy*100)

    cm = confusion_matrix(Y_pred,Y_test)
    print("Confusion matrix is: ",cm)

    ShowGraphs(df,Y_test,Y_pred)

###################################################################
# Function Name : DisplayInfo
# Description   : Displays a formatted title with separators for
#                 better readability in console output.
# Parameters    :
#       title : Heading text to be displayed
# Returns       : None
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def DisplayInfo(title):
    print("\n" + "="*82)
    print(title)
    print("="*82)

###################################################################
# Function Name : ShowData
# Description   : Displays basic information about the dataset
#                 including first five rows, shape, column names
#                 and missing values.
# Parameters    :
#       df      : Pandas DataFrame containing the dataset
#       message : Heading message to display
# Returns       : None
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def ShowData(df,message):
    DisplayInfo(message)
    print("\nFirst Five Rows of Dataset:")
    print(df.head())

    print("\nShape of Dataset: ")
    print(df.shape)

    print("\nColumn names: ")
    print(df.columns.tolist())

    print("\nMissing value in each column: ")
    print(df.isnull().sum())

###################################################################
# Function Name : CleanTitanicData
# Description   : Performs data preprocessing on the Titanic dataset.
#                 Steps include removing unnecessary columns,
#                 handling missing values and encoding categorical
#                 variables into numeric format.
# Parameters    :
#       df : Raw Titanic dataset (Pandas DataFrame)
# Returns       : Cleaned and preprocessed DataFrame
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def CleanTitanicData(df):
    DisplayInfo("Step 2: Original Data")
    print(df.head())

    # Remove unnecessary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be dropped: ")
    print(existing_columns)

    #Drop the unwanted Columns 
    df = df.drop(columns = existing_columns)

    DisplayInfo("Step 2: Data after column Removal")
    print(df.head())

    # Handle Edge Column
    if "Age" in df.columns:
        print("Age Columns before filling missing values")
        print(df["Age"].head(10))

        # coerce -> Invalid Value gets convertes as NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        age_median = df["Age"].median()

        # Replaced missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after pre-processing : ")
        print(df["Age"].head(10))

        # Handle Fare column
        if "Fare" in df.columns:
            print("\nFare Columns before Fare Processing: ")
            print(df["Fare"].head(10))

            df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
            fare_median = df["Fare"].median()
            print("\nMedian of fare column is: ",fare_median)
            df["Fare"] = df["Fare"].fillna(fare_median)

        print("\nFare column after pre-processing : ")
        print(df["Age"].head(10))
              
        # Handle Embarked Column

        if "Embarked" in df.columns:
            print("\nEmbarked Columns before Fare Processing: ")
            print(df["Embarked"].head(10))

            # Convert the Data into String
            df["Embarked"] = df["Embarked"].astype(str).str.strip()
            
            # Remove missing values
            df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)
            
            # Get most Frequent Value
            embarked_mode = df["Embarked"].mode()[0]
            print("\nMode of Embarked Columns: ",embarked_mode)
            df["Embarked"] = df["Embarked"].fillna(embarked_mode)

            print("\nEmbarked column after pre-processing : ")
            print(df["Embarked"].head(10))

        # Handle Sex Column
        if "Sex" in df.columns:
            print("\nSex Columns before Fare Processing: ")
            print(df["Sex"].head(10))

            df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")

        print("\nSex column after pre-processing : ")
        print(df["Sex"].head(10))

        DisplayInfo("Data after Pre-Processing")
        print(df.head())

        print("\nMissing values after Pre-Processing: ")
        print(df.isnull().sum())
    
    # Encode Embarked Column
    df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)

    print("Shape of the Dataset: ",df.shape)

    # Convert boolean columns into Integers
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\nData After Encoding : ")
    print(df.head())
    return df
    
###################################################################
# Function Name : MarvellousTitanicLogistic
# Description   : Main pipeline controller which loads the dataset,
#                 displays raw data, performs preprocessing and
#                 trains the machine learning model.
# Parameters    :
#       DataPath : Path of the Titanic dataset CSV file
# Returns       : None
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1: Loading the Dataset")
    df = pd.read_csv(DataPath)

    ShowData(df,"Initial Datset: ")

    df = CleanTitanicData(df)

    df = TrainTitanicModel(df)

###################################################################
# Function Name : MarvellousTitanicLogistic
# Description   : Main pipeline controller which loads the dataset,
#                 displays raw data, performs preprocessing and
#                 trains the machine learning model.
# Parameters    :
#       DataPath : Path of the Titanic dataset CSV file
# Returns       : None
# Author        : Atharv Tushar Bhosale
# Date          : 14/03/2026
###################################################################

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")
    
if __name__ =="__main__":
    main()
