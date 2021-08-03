from .mean import Mean
from pymongo import MongoClient
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests 
from scipy.stats import ttest_1samp
import numpy as np

class hypo1:
    def __init__(self,mean):
## h0 is mean time for a click is 3sec
## h1 is its not.
        self.time=[]
        self.time.append(mean)
        #ztest,pval=stests.ztest(df[''])

    def ttests(self,)

m=Mean()

     