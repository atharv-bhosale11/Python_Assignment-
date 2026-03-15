import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler


#######################################################################
# Function Name : LoadDataset
# Description   : Loads dataset from the CSV file
# Parameters    : Datapath - path of dataset file
# Returns       : DataFrame object
# Author        : Atharv Tushar Bhosale
# Date          : 15/03/2026
#######################################################################

def LoadDataset(Datapath):

    df = pd.read_csv(Datapath)

    print("Dataset Loaded Successfully")
    print(df.head())

    return df


#######################################################################
# Function Name : CleanDataset
# Description   : Removes missing values from dataset
# Parameters    : df - pandas dataframe
# Returns       : Clean dataframe
#######################################################################

def CleanDataset(df):

    df.dropna(inplace=True)

    print("Dataset Cleaned")
    print("Total Records:",df.shape[0])
    print("Total Columns:",df.shape[1])

    return df


#######################################################################
# Function Name : SplitFeaturesTarget
# Description   : Separates independent and dependent variables
# Parameters    : df - pandas dataframe
# Returns       : X (features), Y (target)
#######################################################################

def SplitFeaturesTarget(df):

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape)

    return X,Y


#######################################################################
# Function Name : SplitTrainingTesting
# Description   : Splits dataset into training and testing data
# Parameters    : X,Y
# Returns       : X_train,X_test,Y_train,Y_test
#######################################################################

def SplitTrainingTesting(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,Y,test_size=0.2,random_state=42,stratify=Y)

    print("Training and Testing data created")

    return X_train,X_test,Y_train,Y_test


#######################################################################
# Function Name : FeatureScaling
# Description   : Performs standardization of input features
# Parameters    : X_train,X_test
# Returns       : X_train_scaled,X_test_scaled
#######################################################################

def FeatureScaling(X_train,X_test):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Feature Scaling Completed")

    return X_train_scaled,X_test_scaled


#######################################################################
# Function Name : FindBestK
# Description   : Finds best value of K using accuracy comparison
# Parameters    : X_train_scaled,Y_train,X_test_scaled,Y_test
# Returns       : best_k , accuracy_scores
#######################################################################

def FindBestK(X_train_scaled,Y_train,X_test_scaled,Y_test):

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train_scaled,Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test,Y_pred)

        accuracy_scores.append(accuracy)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best K value:",best_k)

    return best_k,K_values,accuracy_scores


#######################################################################
# Function Name : PlotGraph
# Description   : Plots graph between K values and accuracy
# Parameters    : K_values,accuracy_scores
# Returns       : None
#######################################################################

def PlotGraph(K_values,accuracy_scores):

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker='o')

    plt.title("K Value vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(K_values)

    plt.show()


#######################################################################
# Function Name : TrainFinalModel
# Description   : Trains KNN model using best K value
# Parameters    : best_k,X_train_scaled,Y_train,X_test_scaled
# Returns       : Predictions
#######################################################################

def TrainFinalModel(best_k,X_train_scaled,Y_train,X_test_scaled):

    model = KNeighborsClassifier(n_neighbors=best_k)

    model.fit(X_train_scaled,Y_train)

    Y_pred = model.predict(X_test_scaled)

    return Y_pred


#######################################################################
# Function Name : EvaluateModel
# Description   : Evaluates model using accuracy, confusion matrix
#                 and classification report
# Parameters    : Y_test,Y_pred
# Returns       : None
#######################################################################

def EvaluateModel(Y_test,Y_pred):

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy:",accuracy*100)

    print("Confusion Matrix:")
    print(confusion_matrix(Y_test,Y_pred))

    print("Classification Report:")
    print(classification_report(Y_test,Y_pred))


#######################################################################
# Function Name : MarvellousClassifier
# Description   : Main pipeline controller for the classifier
# Parameters    : Datapath
# Returns       : None
#######################################################################

def MarvellousClassifier(Datapath):

    df = LoadDataset(Datapath)

    df = CleanDataset(df)

    X,Y = SplitFeaturesTarget(df)

    X_train,X_test,Y_train,Y_test = SplitTrainingTesting(X,Y)

    X_train_scaled,X_test_scaled = FeatureScaling(X_train,X_test)

    best_k,K_values,accuracy_scores = FindBestK(
        X_train_scaled,Y_train,X_test_scaled,Y_test)

    PlotGraph(K_values,accuracy_scores)

    Y_pred = TrainFinalModel(best_k,X_train_scaled,Y_train,X_test_scaled)

    EvaluateModel(Y_test,Y_pred)


#######################################################################
# Function Name : main
# Description   : Entry point of the program
#######################################################################

def main():

    print("Wine Classifier using KNN")

    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()
