import math
from scipy.stats import t
# function for calculating the t-test for two independent samples
def independent_ttest(mean1, se1, mean2,se2, df):

	sed = math.sqrt(se1**2.0 + se2**2.0)
	t_stat = (mean1 - mean2) / sed
	p = (1.0 - t.cdf(abs(t_stat), df)) * 2.

	return t_stat, round(p,4)

print(independent_ttest(10.43,0.58,9.78,0.54,58))