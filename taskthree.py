import pandas as pd
import numpy as np
onefile = pd.read_csv("Salary_Data.csv")
print(onefile)
#print(pd.DataFrame.equals(onefile))
df = pd.DataFrame(onefile)
print(df)

index = df.index[df['Salary'].apply(np.isnan)]
print(index)

#check if any null value is present
a = df.isnull().values.any()
print(a)



mean = df["Salary"].mean()
print(mean)

updateddataframe = df.fillna(mean)