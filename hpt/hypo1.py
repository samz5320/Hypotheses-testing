from .mean import Mean
from pymongo import MongoClient
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests 
class hypo1:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://sanjayam:123@cluster0.icwhc.mongodb.net/test")
        self.db = self.client['mydb1']

## h0 is mean time for a click is 3sec
## h1 is its not.

        ztest,pval=stests.ztest(df[''])
     