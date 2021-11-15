from data_transformation import generate_table_final
import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


table_final = generate_table_final()
#Train/test split
table_final_TRAIN = table_final[:245]
table_raw_TEST = table_raw[-6:]
variables = ['CES0000000039', 'LCEAPR01USM189S', 'LNS12027714',
             'TCU', 'USEPUINDXM', 'AWHNONAG', 'LNU01300012','LNS11300060','LNS11324230','JTS1000QUR', 'CPIAUCSL', 'JTSJOR']

table_raw = build_seperations_table(variables)


def model(table_final_TRAIN):
    """
    Function to create the model
    args: table_final_TRAIN (pd.DataFrame)
    returns: model_4 (object)
    """
    formula = 'quits ~  women_ratio + lfp_25_54 + job_openings_inversesqrt'
    model4 = ols(formula = formula, data = table_final_TRAIN)
    model_4 = model4.fit(cov_type = 'HAC', cov_kwds = {'maxlags':None}, use_t=True)

    return model_4
