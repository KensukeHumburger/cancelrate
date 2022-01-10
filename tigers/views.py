from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
from django.http import HttpResponse
from django.template import loader

#pred_tigers.pyからコピペ#######################################
from pandas import DataFrame
# 機械学習モジュール
import sklearn
import pickle
import xgboost as xgb
from sklearn.model_selection import cross_validate, KFold
import pandas as pd

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
####################################################################

def index(request):
    return render(request, 'tiger/index.html', {})

def predict_input(request):
    #import PredTigers
    return render(request, 'tiger/index.html')

def predict(request):
    if request.method == 'POST':
        #import PredTigers
        hi = request.POST.get('hi')
        low = request.POST.get('low')
        rain = request.POST.get('rain')
        snow = request.POST.get('snow')

        #param
        params = {'hi':hi, 'low':low, 'rain':rain, 'snow':snow}
        print(params)
        
        pred =PredTigers()
        model =pred.load_model()
        df = pred.load_data(params)
        tigers = model.predict(df)
        
        percent = tigers * 100
        for x in percent: # リストを[]なしで表示
            print(x)
        cancelrate = (round(x,1))

        return render(request, 'tiger/predict_out.html',     # 使用するテンプレート
                  {'tigers': cancelrate })         # テンプレートに渡すデータ
    else:
        return HttpResponse('predict')
