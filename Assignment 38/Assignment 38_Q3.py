import pandas as pd
average_study_hours = df["StudyHours"].mean()
print("Avergae study hours: ",average_study_hours)

average_attendance = df["Attendance"].mean()
print("Average attendance: ",average_attendance)

max_score = df["PreviousScore"].max()
print("Maximum previous score: ",max_score)

min_hours = df["SleepHours"].min()
print("Minimum sleep hours: ",min_hours)
