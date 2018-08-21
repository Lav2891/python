import pandas as pd
import datetime

def get_quarter(get_date):
    month = get_date.month
    year = get_date.year
    day = get_date.day
    quarter = pd.Timestamp(datetime.date(year, month, day)).quarter
    output = quarter
    return(output)
 
def main():
    date_entry = input()
    year, month, day = map(int, date_entry.split('-'))
    get_date = datetime.date(year, month, day)
    output = get_quarter(get_date)
    
if __name__ == "__main__":
    main()