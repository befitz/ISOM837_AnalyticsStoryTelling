from fred_data_extract import build_seperations_table
import pandas as pd
import numpy as np


def create_transformed_table(table_raw):
  """
  Function to transform the variables which improve skewness
  args: table_raw (pd.DataFrame)
  returns: table_transformed (pd.DataFrame)
  """
  table_transformed = pd.DataFrame()
  table_transformed['women_ratio'] = table_raw['women_ratio'] #normalizing does not reduce the skewness
  table_transformed['hourly_earn'] = table_raw['hourly_earn'] #normalizing does not reduce the skewness
  table_transformed['lfp_25_54'] = table_raw['lfp_25_54'] #normalizing does not reduce the skewness
  table_transformed['lfp_16_19_inversesqrt'] = 1/np.sqrt(table_raw['lfp_16_19']) #normalizing reduces the skewness
  table_transformed['lfp_0ver55_inversesqrt'] = 1/np.sqrt(table_raw['lfp_0ver55']) #normalizing reduces the skewness
  table_transformed['cap_utilization'] = table_raw['cap_utilization'] #normalizing does not reduce the skewness
  table_transformed['hours_worked'] = table_raw['hours_worked'] #normalizing does not reduce the skewness
  table_transformed['cpi'] = table_raw['cpi'] #normalizing does not reduce the skewness
  table_transformed['self_employed_inversesqrt'] = 1/np.sqrt(table_raw['self_employed']) #normalizing reduces the skewness
  table_transformed['policy_uncertainty_inversesqrt'] = 1/np.sqrt(table_raw['policy_uncertainty']) #normalizing reduces the skewness
  table_transformed['job_openings_inversesqrt'] = 1/np.sqrt(table_raw['job_openings']) #normalizing reduces the skewness
  table_transformed['quits'] = table_raw['quits'] #normalizing does not reduce the skewness

  return table_transformed


def standardize_data(series):
  """
  Function to standardize a series of the dataframe.
  formula is Xchanged = (x-mean)/stdev
  args: series (pd.Series) indexed by 'Date'
  returns: stand_series (pd.Series)
  """
  xmin = np.min(series)
  xmax = np.max(series)
  stand_series = []
  for i in series:
    stand_series.append((i-xmin)/(xmax-xmin))
  standardized_series = pd.Series(stand_series)

  return standardized_series


def standardize_table(df):
  """
  Function to standardize a dataframe
  args: df (pd.DataFrame)
  returns: table_standardized (pd.DataFrame)
  """
  table_standardized= pd.DataFrame()
  for column in df.columns:
      standard = standardize_data(df[f'{column}'])
      table_standardized[f'{column}'] = standard
  table_standardized.reset_index()

  return table_standardized

def generate_table_final(table_raw):
    table_transformed = create_transformed_table(table_raw)
    table_final = standardize_table(table_transformed)
    table_final = table_final.dropna()

    return table_final
