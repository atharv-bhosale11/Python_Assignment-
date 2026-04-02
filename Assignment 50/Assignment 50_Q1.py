import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

Border = "-"*70

#--------------------------------------------------------
# Step 1: Load and Explore the Dataset
#--------------------------------------------------------

print(Border)
print("Step 1: Load the Dataset")
print(Border)

df = pd.read_csv("bank-full.csv", sep=';')
print(df.head())

# Handle missing values
categorical_cols = df.select_dtypes(include=['object','string']).columns
df[categorical_cols] = df[categorical_cols].replace('unknown', np.nan)

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("Missing Values:")
print(df.isnull().sum())

print("Basic Statistics:")
print(df.describe())

print("All Column Info:")
print(df.describe(include='all'))

print("Class Distribution:")
print(df['y'].value_counts())

sns.countplot(x='y', data=df)
plt.title("Class Distribution")
plt.show()

#--------------------------------------------------------
# Step 2: Encoding
#--------------------------------------------------------

print(Border)
print("Step 2: Encoding")
print(Border)

le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

#--------------------------------------------------------
# Step 3: Split Data
#--------------------------------------------------------

print(Border)
print("Step 3: Split Data")
print(Border)

X = df.drop('y', axis=1)
Y = df['y']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#--------------------------------------------------------
# Step 4: Train Models
#--------------------------------------------------------

print(Border)
print("Step 4: Train Models")
print(Border)

# Logistic Regression
model_LR = LogisticRegression()
model_LR.fit(X_train, Y_train)
Y_pred_LR = model_LR.predict(X_test)

# KNN
model_KNN = KNeighborsClassifier(n_neighbors=5)
model_KNN.fit(X_train, Y_train)
Y_pred_KNN = model_KNN.predict(X_test)

# Random Forest
model_RF = RandomForestClassifier()
model_RF.fit(X_train, Y_train)
Y_pred_RF = model_RF.predict(X_test)

#--------------------------------------------------------
# Step 5: Evaluation
#--------------------------------------------------------

print(Border)
print("Step 5: Evaluation")
print(Border)

print("Logistic Accuracy:", accuracy_score(Y_test, Y_pred_LR))
print("KNN Accuracy:", accuracy_score(Y_test, Y_pred_KNN))
print("Random Forest Accuracy:", accuracy_score(Y_test, Y_pred_RF))
print(Border)

print("Confusion Matrix - Logistic:\n", confusion_matrix(Y_test, Y_pred_LR))
print("Confusion Matrix - KNN:\n", confusion_matrix(Y_test, Y_pred_KNN))
print("Confusion Matrix - RF:\n", confusion_matrix(Y_test, Y_pred_RF))
print(Border)

print("Logistic Report:\n", classification_report(Y_test, Y_pred_LR))
print("KNN Report:\n", classification_report(Y_test, Y_pred_KNN))
print("RF Report:\n", classification_report(Y_test, Y_pred_RF))
print(Border)

# ROC AUC 
Y_prob_LR = model_LR.predict_proba(X_test)[:,1]
Y_prob_KNN = model_KNN.predict_proba(X_test)[:,1]
Y_prob_RF = model_RF.predict_proba(X_test)[:,1]

print("AUC Logistic:", roc_auc_score(Y_test, Y_prob_LR))
print("AUC KNN:", roc_auc_score(Y_test, Y_prob_KNN))
print("AUC RF:", roc_auc_score(Y_test, Y_prob_RF))
print(Border)

#--------------------------------------------------------
# Step 6: Visualization
#--------------------------------------------------------

print(Border)
print("Step 6: Visualization")
print(Border)

plt.figure(figsize=(15,4))

plt.subplot(1,3,1)
sns.heatmap(confusion_matrix(Y_test, Y_pred_LR), annot=True, fmt='d', cmap='Blues')
plt.title("Logistic")

plt.subplot(1,3,2)
sns.heatmap(confusion_matrix(Y_test, Y_pred_KNN), annot=True, fmt='d', cmap='Greens')
plt.title("KNN")

plt.subplot(1,3,3)
sns.heatmap(confusion_matrix(Y_test, Y_pred_RF), annot=True, fmt='d', cmap='Oranges')
plt.title("Random Forest")

plt.show()

# ROC Curves
fpr_LR, tpr_LR, _ = roc_curve(Y_test, Y_prob_LR)
fpr_KNN, tpr_KNN, _ = roc_curve(Y_test, Y_prob_KNN)
fpr_RF, tpr_RF, _ = roc_curve(Y_test, Y_prob_RF)

plt.figure(figsize=(8,6))

plt.plot(fpr_LR, tpr_LR, label="Logistic (AUC=" + str(round(roc_auc_score(Y_test, Y_prob_LR),2)) + ")")
plt.plot(fpr_KNN, tpr_KNN, label="KNN (AUC=" + str(round(roc_auc_score(Y_test, Y_prob_KNN),2)) + ")")
plt.plot(fpr_RF, tpr_RF, label="RF (AUC=" + str(round(roc_auc_score(Y_test, Y_prob_RF),2)) + ")")

plt.plot([0,1], [0,1], linestyle='--')

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()

plt.show()
