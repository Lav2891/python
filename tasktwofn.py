import pandas as pd

def getinput(filename, dlimiter, colname, column_toprocess):
    if not dlimiter: 
        df = pd.DataFrame(filename)
    else:
        df = pd.DataFrame(filename,sep=dlimiter)
        univariate(df, colname, column_toprocess)
        
def univariate(df, colname, column_toprocess):
    #Add a new column with desired numbers and save in colname[1] name
    newcolumn = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    df[colname[1]] = pd.Series(newcolumn, index=df.index)
    
    #Replace null value with a value (0 here)
    df= df.fillna(0)
        
    #get the length of dataframes column
    newcol_length = len(df[colname[1]])
    
    #Define an empty list
    output_column = []
    
    #Add the elements of both the columns and store in the created empty list
    for x in range(newcol_length):
        value_one = df.colname[2][x]
        value_two = df.newcol_name[x]
        value_sum = float(value_one)+float(value_two)
        output_column.append(value_sum)
    
    #Add the output column to the dataframe
    df[colname[3]] = pd.Series(output_column, index=df.index)
        
def main():
    dlimiter = ";"
    filename = "C:/Users/Student/polls/Salary_Data.csv"
    columnname = "Salary, Yearsofexperience"
    column_toprocess = "Salary"
    colname = columnname.split(',')
    getinput(filename, dlimiter, colname, column_toprocess)
    
if __name__ == "__main__":
    main()