import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
sns.scatterplot(x="StudyHours",y="PreviousScore",data=df,color="Red",s=100)

plt.title("Study Hours vs Previous Score")
plt.xlabel("Hours Studied")
plt.ylabel("Previous Score")
plt.grid(True)

plt.show()
