import pandas as pd

print("Percentage of Passed and Failed Students: ",df["FinalResult"].value_counts(normalize=True)*100)
