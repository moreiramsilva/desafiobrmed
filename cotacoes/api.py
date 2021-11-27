import requests
from datetime import date, timedelta
from . models import historicalRates 

def apiVat():
    today = date.today()
    for i in range(0,7):
        #Define o dia da busca na API.
        currentDate =  today - timedelta(days=i)
        #Verifica se dia atual é dia de semana [pois não há cotações em finais de semana].
        if currentDate.weekday() < 5:
            #Verificação do DIA na base de dados.
            histRates = historicalRates.objects.filter(date=currentDate).count()
            if histRates == 0:
                #Chamada da API VAT, com a BASE USD e a data.
                response = requests.get('https://api.vatcomply.com/rates?base=USD&date='+str(currentDate))
                #Status Code da API.
                if response.status_code == 200:
                    data =  response.json()
                    item = historicalRates(
                    date = data['date'],
                    base = data['base'],
                    eur = data['rates']['EUR'],
                    usd = data['rates']['USD'],
                    jpy = data['rates']['JPY'],
                    brl = data['rates']['BRL'],                     
                    )
                    item.save()
                else:
                    print('Erro chamada API')