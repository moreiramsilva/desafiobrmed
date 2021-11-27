from django.shortcuts import render
from .models import historicalRates 
from django.utils import timezone


# Create your views here.
def historicalRates(request):
    histRates = historicalRates.objects.filter(date__gte=timezone.now()-5).order_by('date') 
    return render(request, 'cotacoes/index.html', {'histRates':histRates})