from django.shortcuts import render
from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import historicalRates
from . import api
from . import serializers
from . import form

#View do select ALL.
def index(request):
    #Request da API VAT
    api.apiVat()
    
    selected = {}
    try:    
        if request.GET is not None and request.GET['currency_field'] is not None:
            selected = selectCurrency(request.GET['currency_field'], request)
    except:
        print('Nao ha parametros')
    
    #Select na base de dados
    today = date.today()
    currentDate =  today - timedelta(days=5)
    histRates = historicalRates.objects.filter(date__gte=currentDate).order_by('date')
    
    #Montando Context
    context = {}
    context['form'] = form.CurrencyForm()
    context['data'] = {'histRates':histRates}
    context['selected'] = selected
    
    #Render do HTML
    return render(request, 'cotacoes/index.html', context)

def selectCurrency(item, request):
    histRates = {}
    if item is not None:
        today = date.today()
        currentDate =  today - timedelta(days=5)
        if item == '1':
            print(item)
            #Select BRL na base de dados
            histRates = historicalRates.objects.filter(date__gte=currentDate).order_by('date')
            data = serializers.BrlSerializer(histRates, many=True).data
            return data
            
        if item == '2':
            print(item)
            #Select BRL na base de dados
            histRates = historicalRates.objects.filter(date__gte=currentDate).order_by('date')
            data = serializers.EurSerializer(histRates, many=True).data
            return data
            
        if item == '3':
            print(item)
            #Select BRL na base de dados
            histRates = historicalRates.objects.filter(date__gte=currentDate).order_by('date')
            data = serializers.JpySerializer(histRates, many=True).data
            return data
                        
        else:
            return render(request, 'cotacoes/index.html')