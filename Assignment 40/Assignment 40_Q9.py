import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "--"*40

#######################################################################
# Step 1: Load the Dataset
#######################################################################

print(Border)
print("Step 1: Load the Dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)
print("Datasets get loaded Successfully!!!!!")

#######################################################################
# Step 2: Create New Feature (PerformanceIndex)
#######################################################################

print(Border)
print("Step 1.5: Creating PerformanceIndex Feature")
print(Border)

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

print("New column added successfully!")
print(df[["StudyHours","Attendance","PerformanceIndex"]].head())

#######################################################################
# Step 3: Data Analysis
#######################################################################

print(Border)
print("Step2: Data Analysis")
print(Border)

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"   # ✅ NEW FEATURE INCLUDED
]

X = df[feature_cols]
Y = df["FinalResult"]


#######################################################################
# Step 4: Train and Test Split
#######################################################################

print(Border)
print("Step 4: Train and Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.4,
    random_state=42
)

print("Data Splitting Activity Done!!!!!")

print("X Shape :", X.shape)
print("Y Shape :", Y.shape)
print("X_train :", X_train.shape)
print("X_test :", X_test.shape)
print("Y_train :", Y_train.shape)
print("Y_test :", Y_test.shape)

#######################################################################
# Step 5: Model Training
#######################################################################

print(Border)
print("Step 5: Model Training")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=10
)

print("Model Successfully Created:", model)

model.fit(X_train, Y_train)
print("Model Training Completed!!!!!")

#######################################################################
# Step 6: Prediction
#######################################################################

print(Border)
print("Step 6: Prediction on X_test")
print(Border)

y_pred = model.predict(X_test)
print("Predicted Values:", y_pred)

#######################################################################
# Step 7: Accuracy Calculation
#######################################################################

print(Border)
print("Step 7: Accuracy Calculation")
print(Border)

accuracy = accuracy_score(Y_test, y_pred)
print("Your Accuracy is:", accuracy * 100)




