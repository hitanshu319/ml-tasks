#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("student.csv")
x=df
print(x)
exp=[0.2,0.3,0,0.1]
plt.pie(df.iloc[0:,1],labels=df.iloc[0:,0],explode=exp,autopct="%1.1f%%",shadow=True)
plt.legend()
plt.show()

