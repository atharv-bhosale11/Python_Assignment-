import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

new_student = [[6,85,66,7,7]]

pred = model.predict(new_student)

if pred [0]==1:
    print("Student Will pass")
else:
    print("Student will Fail")
