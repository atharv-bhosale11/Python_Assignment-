import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
