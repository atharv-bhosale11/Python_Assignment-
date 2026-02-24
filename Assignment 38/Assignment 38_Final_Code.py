import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
print("Initial Entries from Dataset: ")
print(df.head())    # Gives first five entriesand tail() gives last 5 entries
print(df.tail())    # # Gives Last five entriesand tail() gives last 5 entries

print("Shape of Dataset : ",df.shape)
print("Column Names : ",list(df.columns))
print("Data types of Column: ",df.dtypes)


#######################################################################
# Step 2: Analysis of Data
#######################################################################

print(Border)
print("Step 2: Analysis of Data")
print(Border)

totalstudent = len(df)
print("Total Number of student :",totalstudent)

passed_students = df[df["FinalResult"] == 1].shape[0]
print("Passing Number of Students: ",passed_students)
failed_students = df[df["FinalResult"] == 0].shape[0]
print("Passing Number of Students: ",failed_students)

#######################################################################
# Step 3: Stastical Analysis of Data
#######################################################################

print(Border)
print("Step 3: Stastical Analysis of Data")
print(Border)

average_study_hours = df["StudyHours"].mean()
print("Avergae study hours: ",average_study_hours)

average_attendance = df["Attendance"].mean()
print("Average attendance: ",average_attendance)

max_score = df["PreviousScore"].max()
print("Maximum previous score: ",max_score)

min_hours = df["SleepHours"].min()
print("Minimum sleep hours: ",min_hours)

#######################################################################
# Step 4: Calculating percentage of Pass fail
#######################################################################

print(Border)
print("Step 4: Calculating percentage of Pass fail")
print(Border)

print("Percentage of Passed and Failed Students: ",df["FinalResult"].value_counts(normalize=True)*100)

#######################################################################
# Step 5: Plotting Histogram
#######################################################################

print(Border)
print("Step 5: Plotting Histogram")
print(Border)

plt.figure(figsize=(8,5))

sns.histplot(df["StudyHours"],bins=10,kde=False,color="yellow")
plt.show()

#######################################################################
# Step 6: Scatter Plot
#######################################################################

print(Border)
print("Step 6: Scatter Plot")
print(Border)

plt.figure(figsize=(8,6))
sns.scatterplot(x="StudyHours",y="PreviousScore",data=df,color="Red",s=100)

plt.title("Study Hours vs Previous Score")
plt.xlabel("Hours Studied")
plt.ylabel("Previous Score")
plt.grid(True)

plt.show()

#######################################################################
# Step 7: Box Plot
#######################################################################

print(Border)
print("Step 7: Box Plot")
print(Border)

sns.boxplot(data=df,x="Attendance")
plt.title("Student Performance ML")
plt.show()

#######################################################################
# Step 8: Relationship between Assignment Completed and Final Result
#######################################################################

print(Border)
print("Step 8: Relationship between Assignment Completed and Final Result")
print(Border)

plt.figure(figsize=(8,6))
sns.regplot(
    data=df,
    x="AssignmentsCompleted",
    y="FinalResult",
    scatter_kws={'alpha':0.5,'color': 'blue'},
    line_kws={'color':'red'}
)

plt.title("Relationship between Assignment Completed and Final Result")
plt.xlabel("Number of Assignment Completed",fontsize=10)
plt.ylabel("Final Results",fontsize=10)

plt.show()

#######################################################################
# Step 9: Relationship between Sleep Hours and Final Result
#######################################################################

print(Border)
print("Step 9: Relationship between Sleephours and Final Result")
print(Border)

plt.figure(figsize=(8,6))
sns.regplot(
    data=df,
    x="SleepHours",
    y="FinalResult",
    scatter_kws={'alpha':0.5,'color': 'blue'},
    line_kws={'color':'red'}
)

plt.title("Relationship between Sleep Hours and Final Result")
plt.xlabel("Sleep Hours",fontsize=10)
plt.ylabel("Final Results",fontsize=10)

plt.show()
