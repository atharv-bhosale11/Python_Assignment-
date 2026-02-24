import pandas as pd

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
