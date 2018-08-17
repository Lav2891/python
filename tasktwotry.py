import pandas as pd

def getinput(filename, dlimiter, colname, column_desiredname,formula):
    if not dlimiter: 
        df = pd.DataFrame(filename)
    else:
        df = pd.DataFrame(filename,sep=dlimiter)
        univariate(df, colname, column_desiredname, formula)
        
def univariate(df, colname, column_desiredname, formula):
    
    #Replace null value with a value (0 here)
    df= df.fillna(0)
        
    #get the length of dataframes column
    newcol_length = len(df[colname[1]])
    
    #Define an empty list
    output_column = []
    
    #Apply the formula and store in the created empty list
    for x in range(newcol_length):
        Salary = colname[x]
        value_sum = eval(formula)
        output_column.append(value_sum)
    
    #Add the output column to the dataframe
    df[column_desiredname] = pd.Series(output_column, index=df.index)

def main():
    dlimiter = ";"
    filename = "C:/Users/Student/polls/Salary_Data.csv"
    columnname = "Salary, Yearsofexperience"
    column_desiredname = "output"
    formula = "Salary*2"
    colname = columnname.split(',')
    getinput(filename, dlimiter, colname, column_desiredname, formula)
    
if __name__ == "__main__":
    main()