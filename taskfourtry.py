import pandas as pd
import numpy as np

onefile = pd.read_csv("Salary_Data.csv")
print(onefile)
df = pd.DataFrame(onefile)
print(df)

dff = df.fillna(3)

newcolumn = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
dff['cal'] = pd.Series(newcolumn, index=df.index)

newcolumn1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
dff['lac'] = pd.Series(newcolumn1, index=df.index)

d = pd.DataFrame(np.random.randn(50, 7), columns=list('ABCDEFG'))
df2 = dff.columns.get_values()
dl = df2.tolist()

colname=[]
colname.append("Salary")
colname.append("cal")
colname.append("lac")


corr = pd.DataFrame()
for Salary in colname:
    for cal in colname:
            corr.loc[Salary, cal] = dff.corr().loc[Salary, cal]
print(corr)

result = (pd.Series([df['Salary'].corr(df['cal']) for col in df], index=df.columns)
          .abs().sort_values())
