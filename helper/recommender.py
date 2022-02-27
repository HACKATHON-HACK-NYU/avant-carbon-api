from scipy import stats
import numpy as np

CONFIDENCE = 0.75 
def trend_increase(past_data, current_data, confidence) -> bool:
    """ past_data is a numpy array of floats,
    each giving the $ amount spent (in a particular category)
    in a specific week, BEFORE this week. This week's $ spending
    is stored in data. If there is less than 1 - CONFIDENCE chance
    this week's data is >= current_data then we predict that there has been
    a significant increase in spending in this category and return True.
    Returns False otherwise.
    """
    
    # Standardise all data first:
    # past = (past_data - np.mean(past_data))/np.std(x)
        
    a, loc, scale = scipy.stats.gamma.fit(past_data)
    cdf = scipy.stats.gamma.cdf(current_data, a, loc=loc, scale=scale)
    return (cdf >= CONFIDENCE)

# Helper for creating fake data
def gen_data(a, loc, scale, N):
    data = scipy.stats.gamma.rvs(a, loc=loc, scale=scale, size=N)
    return data

# X = gen_data(1, 500, 2, 50)
# y = 600

# print(trend_increase(X, y, 0.75))