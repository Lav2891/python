import pandas as pd

def getinput(onefile, dlimiter, colname):
    if not dlimiter: 
        df = pd.DataFrame(onefile)
        correlation_find(df, colname)
    else:
        df = pd.DataFrame(onefile,sep=dlimiter)
        correlation_find(df, colname)
        
def correlation_find(df, colname):
    #get correlation of columns as matrix
    corr = pd.DataFrame()
    for colname[0] in colname:
        for colname[1] in colname:
            corr.loc[colname[0], colname[1]] = df.corr().loc[colname[0], colname[1]]
    

def main():
    dlimiter = ";"
    filepath = "C:/Users/Student/polls/Salary_Data.csv"
    onefile = pd.read_csv(filepath)
    columnname = "Salary, Yearsofexperience"  #columns for which correlation to be calculated
    colname = columnname.split(',')
    getinput(onefile, dlimiter, colname)
    
if __name__ == "__main__":
    main()