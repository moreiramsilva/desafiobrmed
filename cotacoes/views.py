from django.shortcuts import render
from .models import historicalRates
from . import api
from datetime import date, timedelta


# Create your views here.
def index(request):
    #Request da API VAT
    api.apiVat()
    
    #Select na base de dados
    today = date.today()
    currentDate =  today - timedelta(days=5)
    histRates = historicalRates.objects.filter(date__gte=currentDate).order_by('date')
    
    #Render do HTML
    return render(request, 'cotacoes/index.html', {'histRates':histRates})