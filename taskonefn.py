import pandas as pd
import numpy as np

def getinput(filepath, colname, colone):
    df = pd.DataFrame(filepath)
    univariate(df, colname, colone)
    
def univariate(df, colname, colone):
    
    #To get the Mean
    mean = df[colname].mean()
    
    #To get the Variance
    variance = df[colname].var()
    
    #To get the Standard Deviation
    sd = df[colname].std()
    
    #Find positon with null values
    findnull = df[colname].isnull()

    #To get the number of null values present
    sum = df.isnull().sum()

    #To get the index of the null value
    index = df.index[df[colname].apply(np.isnan)]
    
    #To get the corresponding column name of the null value
    a = df[colone].ix[index[0]]
    
    #Replace null value with a value (3 here)
    dff = df.fillna(3)

    #To get the index of a particular value
    o = dff.loc[dff.Salary == 3.0, colone] 
    
    #To get the minimum value of a column
    mi = df.colname.min()
    
    #To get the maximum value of a column
    ma = df.colname.max()
    
    #To get percentile of the values of a column
    m1 = df.colname.quantile(0.25)
    m2 = df.colname.quantile(0.5)
    m3 = df.colname.quantile(0.75)
    m4 = df.colname.quantile(0.90)
    m5 = df.colname.quantile(0.95)
    m6 = df.colname.quantile(0.99)
    m7 = df.colname.quantile(0.99)
    m8 = df.colname.quantile(0.1)
    
    #put the above values in a Series
    s = pd.Series([mi,m1,m2,m3,ma], index=['min', '25%', '50%', '75%', 'max'])
    
    #Convert series to json
    x = s.to_json()

def main():
    getinput(filepath, colname, colone)
if __name__ == "__main__":
    main()