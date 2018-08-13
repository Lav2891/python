import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn
obj = Series([1,2,3,4,5,6])

mymarks_dict = mymarks.to_dict()
mymarks_dict
newvals = Series(mymarks_dict, index=newsubs)
newvals
import webbrowser
websiteurl = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html'
webbrowser.open(websiteurl)
a=pd.read_csv("C:\\Users\\Student\\polls\\Salary_Data.csv")
DataFrame(friendlist_frame,columns=['Email', 'Location', 'Employer'])
friendlist_frame = pd.read_clipboard()
friendlist_frame
friendlist_frame.columns
#Selecting a column that is not present
DataFrame(friendlist_frame,
          columns=['Email', 'Location', 'Employer'])
friendlist_frame.ix[2]
#Adding the employer column
friendlist_frame['Employer'] = "TCS"

friendlist_frame
import webbrowser
websiteurl = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html'
webbrowser.open(websiteurl)
friendlist_frame = pd.read_clipboard()
friendlist_frame
friendlist_frame.columns


s = pd.Series()
print (s)