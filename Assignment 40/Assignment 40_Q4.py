import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def main():

    Student_Data = {
        "StudyHours": [5,6,7,2,3],
        "Attendance": [88,92,98,65,53],
        "PreviousScore": [55,68,72,49,82],
        "AssignmentsCompleted": [5,7,8,2,6],
        "FinalResult": [0,1,0,1,1],
    }

    df = pd.DataFrame(Student_Data)

    # Features and Target
    X = df.drop("FinalResult", axis=1)
    y = df["FinalResult"]


    model = DecisionTreeClassifier()
    model.fit(X, y)

    New_Students = {
        "StudyHours": [4, 8, 1, 6, 3],
        "Attendance": [85, 95, 50, 90, 60],
        "PreviousScore": [60, 75, 40, 70, 55],
        "AssignmentsCompleted": [6, 9, 1, 7, 4]
    }

    new_df = pd.DataFrame(New_Students)

    predictions = model.predict(new_df)

    # Add predictions to dataframe
    new_df["PredictedResult"] = predictions

    # Convert to readable labels
    new_df["PredictedResult"] = new_df["PredictedResult"].map({1: "Pass", 0: "Fail"})

    print("\n===== New Students Prediction =====\n")
    print(new_df)


if __name__ == "__main__":
    main()
