import pandas as pd
import numpy as np

onefile = pd.read_csv("Salary_Data.csv")
print(onefile)
df = pd.DataFrame(onefile)
print(df)

#Add a new column with random numbers
sLength = len(df['Salary'])
df['interest'] = pd.Series(np.random.randn(sLength), index=df.index)
l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
df['interestone'] = pd.Series(l, index=df.index)

df= df.fillna(0)

yrsexp = len(df['interest'])
oo = []
for x in range(yrsexp):
    y = df.interest[x]
    s = df.Salary[x]
    o = float(y)+float(s)
    #o = float(y)*2
    #print(o)
    oo.append(o)
print(oo)

df['interesttwo'] = pd.Series(oo, index=df.index)

print(df.YearsExperience[4])
i = df.Salary[30]
print(i)
print(type(i))
u= df.fillna(0)
print(type(df.YearsExperience[4]))

all_items = []

for i in range(0,5):
    new_item = x
    all_items.append(new_item)
    print (new_item)
    #print hex(id(new_item))  # print memory address of new_item

print (all_items)


from collections import Counter
Counter('aa') == Counter('aa')
if True:
    print("x")
    
list1 = [[10,13,17],[3,5,1],[13,11,12]]
list1[0][2]
print(list1[0][2])

# expression to be evaluated
expr = input("Enter the function(in terms of x):")
 
    # variable used in expression
x = int(input("Enter the value of x:"))
 
    # evaluating expression
y = eval(expr)
 
    # printing evaluated result
print("y = {}".format(y))