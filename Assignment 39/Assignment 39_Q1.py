import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "--"*40

#######################################################################
# Step 1: Load the Dataset and Displaying
#######################################################################

print(Border)
print("Step 1: Load the Dataset and Displaying")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)
print("Datasets get loaded Successfully!!!!!")

#######################################################################
# Step 2: Importing the Model(Decision Tree Classifier)
#######################################################################

print(Border)
print("Step2: Importing the Model(Decision Tree Classifier)")
print(Border)

feature_cols=[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]        #Independent variables
Y = df["FinalResult"]       #dependent variables

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)


X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.4,       # 0.2 means 20%
    random_state=42      # Shuffle the Data
)

print("Data Splitting Activity Done!!!!!")

print("X - Independent :",X.shape)  
print("Y - Dependent :",Y.shape)   

print("X_train :",X_train.shape)   
print("X_test :",X_test.shape)      

print("Y_train :",Y_train.shape)    
print("Y_test :",Y_test.shape)      


print(" I am using DecisionTreeClassifier") 

#Actual Model Implementation

model = DecisionTreeClassifier(         
    criterion="gini",
    max_depth=3,            #hyper parameter tuning
    random_state=42
)

print("Model Successfully Created: ",model)

model.fit(X_train,Y_train)

print("Model Training Completed!!!!!")
