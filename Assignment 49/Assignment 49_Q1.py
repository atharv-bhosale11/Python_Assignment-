import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import seaborn as sns

Border = "="*70

#--------------------------------------------------------
# Step 1: Load the Dataset
#--------------------------------------------------------

print(Border)
print("Step 1: Load the Datasets")
print(Border)

df = pd.read_csv("diabetes.csv")
print("First Few Records: ")
print(df.head())
print("--------------------------------------------------------------")
print("Column Info: ")
print(df.info())
print("--------------------------------------------------------------")
print("Checking the Null Values: ")
print(df.isnull().sum())
print("--------------------------------------------------------------")
print("Basis Statistics: ")
print(df.describe())
print("--------------------------------------------------------------")
plt.hist(df['Outcome'])
plt.title("Distribution of Target Variable(Outcome)")
plt.xlabel("0 - No Diabetes , 1 - Diabetes")
plt.ylabel("Frequency")
plt.show()

#--------------------------------------------------------
# Step 2: Data Pre-processing
#--------------------------------------------------------

print(Border)
print("Step 2: Data Pre-processing")
print(Border)

cols = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']

for col in cols:
    print(col, ":",(df[col]==0).sum)

df[cols] = df[cols].replace(0,np.nan)

df.fillna(df.mean(),inplace=True)

df.dropna(inplace=True)

print(df.isnull().sum())
print("--------------------------------------------------------------")

X = df.drop('Outcome',axis=1)
Y = df["Outcome"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Standard Scaler Data:  ")
print(X_scaled)

print("Features (X):")
print(X.head())
print("--------------------------------------------------------------")
print("\nTarget (Y):")
print(Y.head())

#--------------------------------------------------------
# Step 3: Model Selection
#--------------------------------------------------------

print(Border)
print("Step 3: Model Selection")
print(Border)

X_train,X_test, Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model_lr = LogisticRegression()
model_lr.fit(X_train,Y_train)
Y_pred = model_lr.predict(X_test)

print("Accuracy of Logistic Regression: ")
print(accuracy_score(Y_pred,Y_test)*100)

model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train,Y_train)
Y_pred_KNN = model_knn.predict(X_test)
print("Accuracy of K-Neighbour Classifier: ")
print(accuracy_score(Y_pred_KNN,Y_test)*100)

#--------------------------------------------------------
# Step 4: Model Evaluation
#--------------------------------------------------------

print(Border)
print("Step 4: Model Evaluation")
print(Border)

print("Accuracy of Logistic Regression: ")
print(accuracy_score(Y_pred,Y_test)*100)
print("Accuracy of K-Neighbour Classifier: ")
print(accuracy_score(Y_pred_KNN,Y_test)*100)
print("Classification report of Logistic Regression: ")
print(classification_report(Y_test,Y_pred))
print("-----------------------------------------------------------")
print("Classification Report of K-Neighbour Classifier: ")
print(classification_report(Y_pred_KNN,Y_test))

cm = confusion_matrix(Y_pred,Y_test)
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix of Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

cm = confusion_matrix(Y_pred_KNN,Y_test)
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix of Logistic Regression")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

#--------------------------------------------------------
# Step 6: Final Output
#--------------------------------------------------------

print(Border)
print("Step 6: Final Output")
print(Border)

print("Predictions:")
print(Y_pred)

results = pd.DataFrame({
    "Actual": Y_test.values,
    "Predicted": Y_pred
})

print("\nResults:")
print(results.head())

results.to_csv("diabetes_predictions.csv", index=False)

print("\nPredictions saved to diabetes_predictions.csv")
