from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'tiger/index.html', {})

def predict_input(request):
    from tigers.include.pred_tigers import PredTigers
    return render(request, 'tiger/index.html')

def predict(request):
    if request.method == 'POST':
        from tigers.include.pred_tigers import PredTigers
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
