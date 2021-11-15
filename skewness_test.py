


def test_skewness(x):
  """
  Function to test the skewness of a series
  args: x Post_Transform class vairable
  """
  skew = 3*(x.mean - x.median)/x.std

  return skew
