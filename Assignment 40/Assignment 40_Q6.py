import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)
print("Dataset loaded successfully!")


feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]        # Independent variables
Y = df["FinalResult"]       # Target variable

# Train-Test Split

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

print("Data Splitting Done!")

print("X Shape:", X.shape)
print("Y Shape:", Y.shape)

# Model Creation

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

print("Model Successfully Created:", model)

# Model Training

model.fit(X_train, Y_train)
print("Model Training Completed!")

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("Y_train:", Y_train.shape)
print("Y_test:", Y_test.shape)

# Prediction


y_pred = model.predict(X_test)
print("\nPredicted Values:", y_pred)



# Misclassified Students

comparison_df = X_test.copy()
comparison_df["Actual"] = Y_test.values
comparison_df["Predicted"] = y_pred

misclassified = comparison_df[
    comparison_df["Actual"] != comparison_df["Predicted"]
]

print("MISCLASSIFIED STUDENTS")

print(misclassified)

mis_count = len(misclassified)
print("\nNumber of Misclassified Students:", mis_count)

# Pattern Observation


if mis_count > 0:
    print("Average values of misclassified students:")
    print(misclassified.mean(numeric_only=True))
else:
    print("No misclassified students found.")

#Analysis Hint:
#Misclassification usually occurs near decision boundaries where student performance is borderline.
