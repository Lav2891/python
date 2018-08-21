import pandas as pd

def getinput(onefile, dlimiter, colname, formula):
    if not dlimiter: 
        df = pd.DataFrame(onefile)
        univariate(df, colname, formula)
    else:
        df = pd.DataFrame(onefile,sep=dlimiter)
        univariate(df, colname, formula)
    
def univariate(df, colname, formula):
    
    #Formula application
    Salary = colname[1]
    output = eval(formula)
    
    #Replace missing value by mean
    updateddataframe = df.fillna(output)

def main():
    dlimiter = ";"
    filepath = "Salary_Data.csv"
    #Mean calculation or anything
    formula = "Salary*2"
    onefile = pd.read_csv(filepath)
    columnname = "Salary, Yearsofexperience"
    colname = columnname.split(',')
    getinput(onefile, dlimiter, colname, formula)
    
if __name__ == "__main__":
    main()