import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

def checkAccuracy(Y_test, Y_pred):
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Model Accuracy:", accuracy*100)

Border = "--"*40

#######################################################################
# Step 1: Load the Dataset
#######################################################################

print(Border)
print("Step 1: Load the Dataset")
print(Border)

DatasetPath = "PlayPredictor.csv"
df = pd.read_csv(DatasetPath)

print("Dataset Loaded Successfully")
print(df)

#######################################################################
# Step 2: Label Encoding
#######################################################################

print(Border)
print("Step 2: Label Encoding")
print(Border)

le = LabelEncoder()

df['Whether'] = le.fit_transform(df['Whether'])
df['Temperature'] = le.fit_transform(df['Temperature'])
df['Play'] = le.fit_transform(df['Play'])

print("Encoded Data:")
print(df)

#######################################################################
# Step 3: Train Test Split
#######################################################################

print(Border)
print("Step 3: Train Test Split")
print(Border)

X = df[['Whether','Temperature']]
Y = df['Play']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

print("Training Data Size:", X_train.shape)
print("Testing Data Size:", X_test.shape)

#######################################################################
# Step 4: Feature Scaling + KNN Training
#######################################################################

print(Border)
print("Step 4: Feature Scaling and Model Training")
print(Border)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

k_value = 3

knn_model = KNeighborsClassifier(n_neighbors=k_value)
knn_model.fit(X_train_scaled, Y_train)

Y_pred = knn_model.predict(X_test_scaled)

print("Prediction:", Y_pred)

new_data = [[2,1]]
new_data_scaled = scaler.transform(new_data)
prediction = knn_model.predict(new_data_scaled)

if prediction[0] == 1:
    print("Prediction: Yes (Play)")
else:
    print("Prediction: No (Do not Play)")

#######################################################################
# Step 5: Model Accuracy
#######################################################################

print(Border)
print("Step 5: Model Accuracy")
print(Border)

def main():
    checkAccuracy(Y_test,Y_pred)
    
if __name__ =="__main__":
    main()
