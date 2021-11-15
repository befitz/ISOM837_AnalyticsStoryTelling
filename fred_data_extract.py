import pandas as pd
import numpy as np
from pandas_datareader import DataReader
from pandas_datareader import data as web
import datetime as dt
from functools import reduce


end = dt.datetime.today()
start = (dt.datetime.now() - dt.timedelta(days = 36500)).strftime("%m-%d-%Y")
dfs = []
def get_fed_data(DataSetName):
  """
  Function to retreive the given datasetname from the FRED API
  args: DataSetName (list)
  returns: fred_data (pd.DataFrame)
  """
  for name in DataSetName:
    fred = web.DataReader(f'{name}', 'fred', start, end)
    fred = fred.reset_index()
    fred = fred.rename(columns={'DATE':'Date'})
    dfs.append(fred)
  final_fred = reduce(lambda left,right: pd.merge(left, right, on=['Date'], how = 'outer'), dfs)

  return final_fred


columnNames = {'TCU': 'cap_utilization',
               'USEPUINDXM': 'policy_uncertainty',
               'CES0000000039': 'women_ratio',
               'LCEAPR01USM189S': 'hourly_earn',
               'AWHNONAG': 'hours_worked',
               'LNU01300012': 'lfp_16_19',
               'LNS11300060': 'lfp_25_54',
               'LNS11324230': 'lfp_0ver55',
               'LNS12027714': 'self_employed',
               'JTS1000QUR': 'quits',
               'CPIAUCSL': 'cpi',
               'JTSJOR':'job_openings'}


def build_seperations_table(variables):
  """
  Function to call the get_fed_data function and columns to create the RAW dataset
  args: variables (list)
  returns: table_raw (pd.DataFrame)
  """
  table_raw = get_fed_data(variables)
  table_raw = table_raw.rename(columns = columnNames)
  table_raw = table_raw.dropna()

  return table_raw
