import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

train_prediction = model.predict(X_train)
test_prediction = model.predict(X_test)

train_accuracy = accuracy_score(Y_train,train_prediction)
print("Training Accuracy is: ",train_accuracy*100)

test_accuracy = accuracy_score(Y_test,test_prediction)
print("Testing Accuracy is: ",test_accuracy*100)
