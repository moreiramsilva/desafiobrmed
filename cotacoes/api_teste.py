import requests
from datetime import date, timedelta
from django.test import TestCase


today = date.today()

if type(today) is date:
    print("Data Atual:", today)

response = requests.get('https://api.vatcomply.com/rates?date='+str(today))

if response.status_code == 200:
    data =  response.json()
    print(data)
    print(data['date'])
    print(data['base'])
    print(data['rates'])
    print(data['rates']['EUR'])
    print(data['rates']['USD'])
    print(data['rates']['JPY'])    
    print(data['rates']['BRL'])
else:
    print('Erro')
    
for i in range(0,7):
    currentDate =  today - timedelta(days=i)
    if currentDate.weekday() < 5:
        print('================[    '+str(currentDate)+'    ]================')
        response = requests.get('https://api.vatcomply.com/rates?base=USD&date='+str(currentDate))
        if response.status_code == 200:
            data =  response.json()
            print(data['date'])
            print(data['base'])
            print(data['rates']['EUR'])
            print(data['rates']['USD'])
            print(data['rates']['JPY'])    
            print(data['rates']['BRL'])    
        else:
            print('Erro')
    if currentDate.weekday() >= 5:
        print('================[    '+str(currentDate)+'    ]================')
        print('Final de Semana, nao ha cotacoes de moedas para o dia atual.')