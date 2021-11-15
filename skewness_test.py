


def test_skewness(x):
  """
  Function to test the skewness of a series
  args: x Post_Transform class vairable
  """
  skew = 3*(x.mean - x.median)/x.std

  return skew

class Post_Transform():
  """
  This class is to provide values for the variables WITH transformation. These values are from the RAW data.
  """
  def __init__(self, series):
    self.std = np.std(series)
    self.median = np.median(series)
    self.mean = np.mean(series)

"""
women_ratio_pt = Post_Transform(table_raw['women_ratio']) #normalizing does not reduce the skewness
hourly_earn_pt = Post_Transform(table_raw['hourly_earn']) #normalizing does not reduce the skewness
lfp_25_54_pt = Post_Transform(table_raw['lfp_25_54']) #normalzing does not reduce skewness
lfp_16_19_pt = Post_Transform(table_transformed['lfp_16_19_inversesqrt']) #normalizing reduces the skewness
lfp_0ver55_pt = Post_Transform(table_transformed['lfp_0ver55_inversesqrt']) #normalizing reduces the skewness
cap_utilization_pt = Post_Transform(table_raw['cap_utilization']) #normalizing does not reduce the skewness
hours_worked_pt = Post_Transform(table_raw['hours_worked']) #normalizing does not reduce the skewness
cpi_pt = Post_Transform(table_raw['cpi'])#normalizing does not reduce the skewness
self_employed_pt = Post_Transform(table_transformed['self_employed_inversesqrt']) #normalizing reduces the skewness
policy_uncertainty_pt = Post_Transform(table_transformed['policy_uncertainty_inversesqrt']) #normalizing reduces the skewness
job_openings_pt = Post_Transform(table_transformed['job_openings_inversesqrt']) #normalizing reduces the skewness
quits_pt = Post_Transform(table_raw['quits']) #normalizing does not reduce the skewness
"""
