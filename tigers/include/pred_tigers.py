# -*- coding: utf-8 -*-
# predict
#import numpy as np
#import numpy.random as random
#import pandas as pd
from pandas import DataFrame

# 機械学習モジュール
import sklearn
import pickle
import xgboost as xgb
from sklearn.model_selection import cross_validate, KFold

#
class PredTigers:
    def __init__(self):
        self.params = {}
    #
    def load_model(self):
        filename = 'tigers/files/model_XGB.pickle'
        model = pickle.load(open(filename, 'rb'))
        return model
    
    def load_data(self, params):
        dat = {'hi':[params['hi']]
        ,'low':[params['low']]
        ,'rain':[params['rain']]
        ,'snow':[params['snow']]
        }
        df = DataFrame(dat)
        df = df.assign(hi = pd.to_numeric(df.hi))
        df = df.assign(low = pd.to_numeric(df.low))
        df = df.assign(rain = pd.to_numeric(df.rain))
        df = df.assign(snow = pd.to_numeric(df.snow))
        #print(df.info() )
        return df
