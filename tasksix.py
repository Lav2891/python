import sys
import argparse
import pandas as pd
import datetime
#import datetime as dt
from dateutil.parser import parse

from datetime import datetime, timedelta
from pytz import timezone

import pytz
date_entry = input('Enter a date ')
print(datetime.datetime.now(pytz.timezone('US/Central')).isoformat())

year, month, day = map(int, date_entry.split('-'))
#datetime.strftime(format)
dfo = datetime.strptime(date_entry, '%Y-%m-%d')
print(dfo)
datetime.datetime.strptime(date_entry, '%Y-%m-%d')
date1 = datetime.date(year, month, day)


def ate(date1):
    print(date1)
    #print("HERE: ",date1.month)
    quarter = pd.Timestamp(datetime.date(year, month, day)).quarter
    #assert quarter == 1
    #print (quarter)
    out = quarter
    return(out)
o = ate(date1) 
print("o",o) 


onefile = pd.read_csv("calander.csv")
print(onefile)
#print(pd.DataFrame.equals(onefile))
df = pd.DataFrame(onefile)
print(df)


xDate = sys.argv[1]
parser=argparse.ArgumentParser()
parser.add_argument('xDate')
args=parser.parse_args()


year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date1 = datetime.date(year, month, day)


parse("2003/09/01")

from datetime import date
today = date.today()
print(today)

import datetime, time
date_entry = input('Enter a date ')
time.mktime(date_entry.toordinal())

dd = int(date_entry)
d = date.fromordinal(dd)
d.isoformat()

d = date.fromordinal(730920) 
d.isoformat()

from datetime import datetime as dt
date_entry = input('Enter a date ')
d = dt.strptime(date_entry, '%Y-%m-%d').date()
x = d.toordinal()
dd = dt.fromordinal(x) 
dd.isoformat()