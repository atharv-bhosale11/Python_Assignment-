import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

sns.histplot(df["StudyHours"],bins=10,kde=False,color="yellow")
plt.show()
