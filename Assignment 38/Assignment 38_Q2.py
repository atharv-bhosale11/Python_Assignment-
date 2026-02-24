import pandas as pd

totalstudent = len(df)
print("Total Number of student :",totalstudent)

passed_students = df[df["FinalResult"] == 1].shape[0]
print("Passing Number of Students: ",passed_students)
failed_students = df[df["FinalResult"] == 0].shape[0]
print("Passing Number of Students: ",failed_students)
