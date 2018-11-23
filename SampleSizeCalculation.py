import numpy as np
from scipy.stats import norm

#H0: deltaC=0 (where deltaC = C1 - C2 is the difference between Harrell's concordance index for DL and conventional parameter models)
#sample size based on Wald-type test statistic for H0, with two-sided alternative [Obuchowski & McClish (1997), Kang et al (2015)]:
#  d = [(za + zb)^2] / [(deltaC/SE_deltaC)^2], where:
#    za : upper a-th percentile of the standard normal distribution
#    zb : upper b-th percentile of the standard normal distribution
#    SE_deltaC : standard error of deltaC estimate
#    d: number of events

deltaC = 0.06
SE_deltaC = 0.1627
alpha_level = .05
power = 0.9
za = norm.ppf(1-(alpha_level/2))   #upper 2.5th percentile of standard normal distribution
zb = norm.ppf(power)               #upper 10th  percentile of the standard normal distribution

d = np.ceil((za + zb)**2 / (deltaC/SE_deltaC)**2)

#from Nd, we compute total N (based on 83% censoring rate)
crt = .83
N  = np.ceil(d * (1/(1-crt)))
