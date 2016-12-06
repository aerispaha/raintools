import pyodbc, csv
import pandas as pd

def write_csv_from_access(MDB, csv_path):
    # MDB = r"F:\code\rainfall\CSORain2010\CSORain2010.mdb";
    DRV = '{Microsoft Access Driver (*.mdb)}';
    PWD = 'pw'

    # connect to db
    con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
    cur = con.cursor()

    # run a query and get the results
    SQL = 'SELECT * FROM tblModelRain;' # your query goes here
    rows = cur.execute(SQL).fetchall()
    cur.close()
    con.close()

    # you could change the mode from 'w' to 'a' (append) for any subsequent queries
    # csv_path = r'F:\code\rainfall\CSORain2010_gauge1.csv'
    with open(csv_path, 'wb') as fou:
        csv_writer = csv.writer(fou) # default field-delimiter is ","
        csv_writer.writerows(rows)


def gage_average_and_rolling_depth(rain_per_gage, rolling_win='6h'):
    """
    return a dataframe with average depth among all the raingages passed in
    and a rolling total volume of the average depth.

    cool
    """

    #convert index to DateTime
    dtime_index = pd.to_datetime(rain_per_gage.index)
    df = rain_per_gage.set_index(dtime_index)

    #fill NANs with 0 so average volume is weights properly (does this make sense?)
    df = df.fillna(0)

    #find the mean of all raingages in each row (axis = 1)
    df['avg_gages'] = df.mean(axis=1)

    #and the rolling total. Pandas handles ragged time-indexed DataFrames now
    rolling_col_name = 'rolling_{}'.format(rolling_win)
    df[rolling_col_name] = df.avg_gages.rolling(rolling_win).sum()

    return df[['avg_gages', rolling_col_name]]

def find_independent_events(rain_gage, event_gap='6h'):
    pass
