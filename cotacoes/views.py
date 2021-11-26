from django.shortcuts import render

# Create your views here.
def historicalRates(request):
    return render(request, 'cotacoes/rates.html', {})