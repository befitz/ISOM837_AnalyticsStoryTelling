from statsmodels.formula.api import ols
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


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
