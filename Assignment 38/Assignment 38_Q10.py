import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
