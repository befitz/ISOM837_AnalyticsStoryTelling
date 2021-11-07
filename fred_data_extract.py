import pandas as pd
import numpy as np
from pandas_datareader import DataReader
from pandas_datareader import data as web
import datetime as dt
from functools import reduce

end = dt.datetime.today()
start = (dt.datetime.now() - dt.timedelta(days = 36500)).strftime("%m-%d-%Y")
dfs = []
def get_fed_data(DataSetName, raw = True):
"""
Function to retrieve the FRED data series for the given dataset code.
args: DataSetName (str), raw (bool) default is True, False will transform to log percentage change
returns: merged collection of variables on a monthly timeframe
"""
    for i in DataSetName:
        fred = web.DataReader(f'{i}', 'fred', start, end)
        fred = fred.reset_index()
        fred = fred.rename(columns={'DATE':'Date'})
    if raw == True:
      pass
    else:
      fred[f'{i}_lnpctchng'] = (np.log(fred[f'{i}'] - np.log(fred[f'{i}'].shift(1)))/np.log(fred[f'{i}'].shift(1)))
      fred = fred.drop(columns = i)
    dfs.append(fred)
  final_fred = reduce(lambda left,right: pd.merge(left, right, on=['Date'], how = 'outer'), dfs)

  return final_fred


variables = ['JTSTSR', 'CES0500000035', 'FEDMINNFRWG','JTSJOR', 'LNS13023706', 'CSUSHPINSA',
'CEU0000000010', 'CES0000000039', 'JTSHIR', 'LCEAPR01USM189S', 'LNS12026619', 'CPIAUCSL', 'CUSR0000SAM2', 'CUSR0000SEEB']

seperations_table_raw = get_fed_data(variables, raw = True)
seperations_table_transformed = get_fed_data(variables, raw = False)

seperations_table_transformed = seperations_table_transformed.dropna()
seperations_table_transformed = seperations_table_transformed.rename(columns = {'JTSTSR_lnpctchng': 'seperations_lnpctchng', 'CES0500000035_lnpctchng': 'hrs_and_earnings_lnpctchng', 'CSUSHPINSA_lnpctchng':'home_price_index_lnpctchng', 'CES0000000039_lnpctchng': 'women_ratio_lnpctchng',
                                                          'FEDMINNFRWG_lnpctchng': 'min_wage_lnpctchng', 'JTSJOR_lnpctchng': 'job_openings_lnpctchnge', 'LNS13023706_lnpctchng': 'leaver_lnpctchng', 'CEU0000000010_lnpctchng': 'women_employed_lnpctchng',
                                                          'JTSHIR_lnpctchng': 'hires_lnpctchng', 'LCEAPR01USM189S_lnpctchng': 'hourly_earn_lnpctchng', 'LNS12026619_lnpctchng': 'multiple_jobs_lnpctchng', 'CPIAUCSL_lnpctchng': 'cpi_lnpctchng', 'CUSR0000SAM2_lnpctchng': 'medical_cpi_lnpctchng',
                                                          'CUSR0000SEEB_lnpctchng': 'education_cpi_lnpctchng'})
seperations_table_raw = seperations_table_raw.rename(columns = {'JTSTSR': 'seperations', 'CES0500000035': 'hrs_and_earnings', 'FEDMINNFRWG': 'min_wage','JTSJOR': 'job_openings', 'LNS13023706': 'leaver', 'CSUSHPINSA': 'home_price_index', 'CEU0000000010': 'women_employed',
                                                                'CES0000000039': 'women_ratio', 'JTSHIR': 'hires', 'LCEAPR01USM189S': 'hourly_earn', 'LNS12026619': 'multiple_jobs', 'CPIAUCSL': 'cpi', 'CUSR0000SAM2': 'medical_cpi', 'CUSR0000SEEB': 'education_cpi'})


seperations_table_raw.to_csv('/Users/brynne/Python/Desktop/Suffolk University/ISOM 837 Data Mining/seperations_table_raw.csv')
seperations_table_transformed.to_csv('/Users/brynne/Python/Desktop/Suffolk University/ISOM 837 Data Mining/seperations_table_transformed.csv')
