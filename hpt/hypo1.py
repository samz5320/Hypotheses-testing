from .mean import Mean
from pymongo import MongoClient
import pandas as pd
from scipy import stats
#from statsmodels.stats import weightstats as stests
from scipy.stats import ttest_1samp
import numpy as np


class Hypo1:
    def __init__(self):
        # h0 is mean time for a click is 3sec
        # h1 is its not.
        m = Mean()
        # self.time = []
        # self.time.append(mean)
        # ztest,pval=stests.ztest(df[''])
        self.ages_all = m.l+m.l1

        #print(self.ages_all)
        #print(len(self.ages_all))
        self.ages_mean=np.mean(self.ages_all)
        #print(self.ages_mean)

        self.tset,self.pval=ttest_1samp(self.ages_all,3.5)

        print("p-values",self.pval)
        s1="we are rejecting null hypothesis"
        s2="we are accepting null hypothesis"
        if self.pval < 0.05:    # alpha value is 0.05 or 5%
            self.op = s1
        else:
            self.op = s2

h=Hypo1()
#print(h)
