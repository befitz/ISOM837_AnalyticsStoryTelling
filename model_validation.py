from data_transformation import *
from model import model

import numpy as np
import pandas as pd

class Test_Values():
  """
  This class is to provide values for the variables WITHOUT transformation. These values are from the RAW data.
  """
  def __init__(self, series):
    self.std = np.std(series)
    self.median = np.median(series)
    self.mean = np.mean(series)
    self.test_val1 = series.iloc[-5] - series.iloc[-6]
    self.test_val2 = series.iloc[-4] - series.iloc[-5]
    self.test_val3 = series.iloc[-3] - series.iloc[-4]
    self.test_val4 = series.iloc[-2] - series.iloc[-3]
    self.test_val5 = series.iloc[-1] - series.iloc[-2]
    self.min = np.min(series)
    self.max = np.max(series)
    self.max_minus_min = np.max(series) - np.min(series)
    self.min_max = (np.min(series) - np.max(series))/ (np.max(series) - np.min(series))



def validation_test2(model,Y,x1,x2,x3, test_number):
  """
  Function to test standardized model with min-max standardization applied.
  For the 3rd variable will de-transform the inverse square root
  args: model (object) , coef (list)
  returns: estimate (float)
  """
  coefficients = model.params
  if test_number == 1:
    _x1 = (coefficients[1]*x1.min_max)*x1.test_val1
    _x2 = (coefficients[2]*x2.min_max)*x2.test_val1
    _x3_ = coefficients[3] * job_openings_inversesqrt.min_max
    __x3 = 1/(_x3_*_x3_) #to de-transform the normalization
    _x3 = __x3*x3.test_val1
    _priorY = table_raw['quits'].iloc[-6]
    _Y = table_raw['quits'].iloc[-5]
  elif test_number == 2:
    _x1 = (coefficients[1]*x1.min_max)*x1.test_val2
    _x2 = (coefficients[2]*x2.min_max)*x2.test_val2
    _x3_ = coefficients[3] * job_openings_inversesqrt.min_max
    __x3 = 1/(_x3_*_x3_) #to de-transform the normalization
    _x3 = __x3*x3.test_val2
    _priorY = table_raw['quits'].iloc[-5]
    _Y = table_raw['quits'].iloc[-4]
  elif test_number == 3:
    _x1 = (coefficients[1]*x1.min_max)*x1.test_val3
    _x2 = (coefficients[2]*x2.min_max)*x2.test_val3
    _x3_ = coefficients[3] * job_openings_inversesqrt.min_max
    __x3 = 1/(_x3_*_x3_) #to de-transform the normalization
    _x3 = __x3*x3.test_val3
    _priorY = table_raw['quits'].iloc[-4]
    _Y = table_raw['quits'].iloc[-3]
  elif test_number == 4:
    _x1 = (coefficients[1]*x1.min_max)*x1.test_val4
    _x2 = (coefficients[2]*x2.min_max)*x2.test_val4
    _x3_ = (coefficients[3]*job_openings_inversesqrt.min_max)
    __x3 = 1/(_x3_*_x3_)
    _x3 = __x3*job_openings.test_val4
    _priorY = table_raw['quits'].iloc[-3]
    _Y = table_raw['quits'].iloc[-2]
  elif test_number == 5:
    _x1 = (coefficients[1]*x1.min_max)*x1.test_val5
    _x2 = (coefficients[2]*x2.min_max)*x2.test_val5
    _x3_ = (coefficients[3]*job_openings_inversesqrt.min_max)
    __x3 = 1/(_x3_*_x3_)
    _x3 = __x3*job_openings.test_val5
    _priorY = table_raw['quits'].iloc[-2]
    _Y = table_raw['quits'].iloc[-1]

  estimate = _x1 + _x2 + _x3 + _priorY
  actual = _Y
  accuracy = 1-(np.abs((estimate-actual)/actual))

  return estimate, actual, accuracy

def results_table(model, Y, x1, x2, x3):
  """
  Function to create a dataframe of the estimates, actuals and results for 5 tests
  """
  model_validation = pd.DataFrame(columns = ['Test', 'Estimate', 'Actual', 'Accuracy'])
  count = 1
  estimate_list = []
  actual_list = []
  accuracy_list = []
  test_list = []
  while count <=5:
    estimate, actual, accuracy = validation_test2(model, Y, x1, x2, x3, count)
    estimate_list.append(estimate)
    actual_list.append(actual)
    accuracy_list.append(accuracy)
    test_list.append(count)
    count +=1

  model_validation['Test'] = test_list
  model_validation['Estimate'] = estimate_list
  model_validation['Actual'] = actual_list
  model_validation['Accuracy'] = accuracy_list

  return model_validation


if __name__ == '__main__':
    variables = ['CES0000000039', 'LCEAPR01USM189S', 'LNS12027714',
                 'TCU', 'USEPUINDXM', 'AWHNONAG', 'LNU01300012','LNS11300060','LNS11324230','JTS1000QUR', 'CPIAUCSL', 'JTSJOR']
    table_raw = build_seperations_table(variables)

    women_ratio = Test_Values(table_raw['women_ratio'])
    job_openings = Test_Values(table_raw['job_openings'])
    quits = Test_Values(table_raw['quits'])
    lfp_25_54 = Test_Values(table_raw['lfp_25_54'])

    table_final = generate_table_final(table_raw)
    #Train/test split
    table_final_TRAIN = table_final[:245]
    table_raw_TEST = table_raw[-6:]

    model = model(table_final_TRAIN)

    df = results_table(model, quits, women_ratio, lfp_25_54, job_openings)
    final_accuracy = (df['Accuracy'].sum())/5

    print("Average Accuracy: %0.2f" % (final_accuracy*100),"%")
    print('Test Table Details:')
    display(df)
