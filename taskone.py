import pandas as pd
import numpy as np
onefile = pd.read_csv("Salary_Data.csv")
print(onefile)
#print(pd.DataFrame.equals(onefile))
df = pd.DataFrame(onefile)
print(df)
#n = lambda df: df[df.isnull().any(axis=1)]


mean = df["Salary"].mean()
print(mean)

variance = df["Salary"].var()
print(variance)

sd = df["Salary"].std()
print(sd)

findnull = df["Salary"].isnull()
print(findnull)

sum = df.isnull().sum()
print(sum)

index = df.index[df['Salary'].apply(np.isnan)]
print(index)
a = df['YearsExperience'].ix[index[0]]
print(a)

dff = df.fillna(3)
print(dff)

o = dff.loc[dff.Salary == 3.0, 'YearsExperience'] 
print(o)

mi = df.Salary.min()
print(mi)

ma = df.Salary.max()
print(ma)

m1 = df.Salary.quantile(0.25)
m2 = df.Salary.quantile(0.5)
m3 = df.Salary.quantile(0.75)
m4 = df.Salary.quantile(0.90)
m5 = df.Salary.quantile(0.95)
m6 = df.Salary.quantile(0.99)
m7 = df.Salary.quantile(0.99)
m8 = df.Salary.quantile(0.1)
print(m1,m2,m3,m4,m5,m6,m7,m8)

#ds = pd.Series([]) 
#for x in range(5):
  #  d = ds.append(pd.Series([]))
   # print(d)
   
s = pd.Series([mi,m1,m2,m3,ma], index=['min', '25%', '50%', '75%', 'max'])
print(s)
x = s.to_json()
print(x)