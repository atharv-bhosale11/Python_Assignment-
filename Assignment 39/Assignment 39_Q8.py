import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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

DatasetPath = "student_performance_ml.csv"  # Giving the path of dataset

df = pd.read_csv(DatasetPath)
print("Datasets get loaded Successfully!!!!!")

#######################################################################
# Step 2: Data Analysis
#######################################################################

print(Border)
print("Step2: Data Analysis")
print(Border)

#Name of Attributes
feature_cols=[              
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]        #Independent variables
Y = df["FinalResult"]       #dependent variables

#######################################################################
# Step 3: Data Visualization
#######################################################################

print(Border)
print("Step 3: Data Visualization")
print(Border)

#Histogram
plt.figure(figsize=(8,5))
sns.histplot(df["StudyHours"],bins=10,kde=False,color="yellow")
plt.show()

#Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(x="StudyHours",y="PreviousScore",data=df,color="Red",s=100)

plt.title("Study Hours vs Previous Score")
plt.xlabel("Hours Studied")
plt.ylabel("Previous Score")
plt.grid(True)
plt.show()

#Box Plot
sns.boxplot(data=df,x="Attendance")
plt.title("Student Performance ML")
plt.show()

#######################################################################
# Step 4: Train and Test Split
#######################################################################

print(Border)
print("Step 4: Train and Test Split")
print(Border)

#Splitting of Data
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.4,       # 0.4 means 40%
    random_state=42      # Shuffle the Data
)

print("Data Splitting Activity Done!!!!!")

print("X Shape : ",X.shape) #(30,5)
print("Y Shape : ",Y.shape) #(30,)
   

print("X_train :",X_train.shape) #(18,5)  
print("X_test :",X_test.shape)   #(12,5)

print("Y_train :",Y_train.shape)    #(18,)
print("Y_test :",Y_test.shape)      #(12,)

#######################################################################
# Step 5: Model Training
#######################################################################

print(Border)
print("Step 5: Model Training")
print(Border)

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

#######################################################################
# Step 6: Prediction
#######################################################################

print(Border)
print("Step 3: Predicting and Displaying result for X_test")
print(Border)

y_pred = model.predict(X_test)
print("Predicted Values",y_pred)

#######################################################################
# Step 7: Accuracy Calculation
#######################################################################

print(Border)
print("Step 7: Accuracy Calculation")
print(Border)

accuracy = accuracy_score(Y_test,y_pred)    #Finding Accuracy
print("Your Accuracy is: ",accuracy*100)

#######################################################################
# Step 8: Confusion Matrix Generation
#######################################################################

print(Border)
print("Step8: Confusion Matrix Generation")
print(Border)

cm = confusion_matrix(Y_test,y_pred)
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix for Student Dataset")
plt.show()

#Conclusion :- Identifying the most effective model for predicting student performance and highlighting the key factors(Attendance,Previous Score,Assignment and Sleephours) 
#On this Dataset I analyse the data over that I implement Decision tree Classifier Model ,find the accuracy, Confusion Matrix as well as makes Visualize Presentation.
