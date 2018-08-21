import pandas as pd

def getinput(onefile, dlimiter, colname):
    if not dlimiter: 
        df = pd.DataFrame(onefile)
        univariate(df, colname)
    else:
        df = pd.DataFrame(onefile,sep=dlimiter)
        univariate(df, colname)
        
def univariate(df, colname):
    #group by the column name
    group_by = df.groupby(df.colname[1])
    
    #get rows containing the value of the column group
    grouped_value = group_by.get_group('value in column')

def main():
    dlimiter = ";"
    filepath = "C:/Users/Student/polls/Salary_Data.csv"
    onefile = pd.read_csv(filepath)
    columnname = "Salary, Yearsofexperience"
    colname = columnname.split(',')
    getinput(onefile, dlimiter, colname)
    
if __name__ == "__main__":
    main()
