import numpy as np
from scipy.stats import spearmanr, ttest_rel
from statsmodels.stats.weightstats import ttost_paired

def ttest_paired(ravasz_values, girvan_newman_values):
    return ttest_rel(ravasz_values, girvan_newman_values)

def tost_test(ravasz_values, girvan_newman_values, diff):
    return ttost_paired(np.array(ravasz_values), np.array(girvan_newman_values), -diff, diff)