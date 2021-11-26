from django.db import models
from django.conf import settings
from django.utils import timezone

class historicalRates(models.Model):
    
    BASE = (
        ('EUR' , 'Euro'),
        ('USD' , 'US Dollar'),
        ('JPY' , 'Japanese Yen'),
        ('BGN' , 'Bulgarian Lev'),
        ('CZK' , 'Czech Koruna'),
        ('DKK' , 'Danish Krone'),
        ('GBP' , 'British Pound'),
        ('HUF' , 'Hungarian Forint'),
        ('PLN' , 'Polish Zloty'),
        ('RON' , 'Romanian Leu'),
        ('SEK' , 'Swedish Krona'),
        ('CHF' , 'Swiss Franc'),
        ('ISK' , 'Icelandic Krona'),
        ('NOK' , 'Norwegian Krone'),
        ('HRK' , 'Croatian Kuna'),
        ('RUB' , 'Russian Ruble'),
        ('TRY' , 'Turkish Lira'),
        ('AUD' , 'Australian Dollar'),
        ('BRL' , 'Brazilian Real'),
        ('CAD' , 'Canadian Dollar'),
        ('CNY' , 'Chinese Yuan'),
        ('HKD' , 'Hong Kong Dollar'),
        ('IDR' , 'Indonesian Rupiah'),
        ('ILS' , 'Israeli New Shekel'),
        ('INR' , 'Indian Rupee'),
        ('KRW' , 'South Korean Won'),
        ('MXN' , 'Mexican Peso'),
        ('MYR' , 'Malaysian Ringgit'),
        ('NZD' , 'New Zealand Dollar'),
        ('PHP' , 'Philippine Piso'),
        ('SGD' , 'Singapore Dollar'),
        ('THB' , 'Thai Baht'),
        ('ZAR' , 'South African Rand')
    )
    
    date = models.DateField()
    base = models.CharField(max_length=3, choices=BASE, default = None)
    usd = models.FloatField(max_length=30, default = None) 
    brl = models.FloatField(max_length=30, default = None)
    eur = models.FloatField(max_length=30, default = None)
    jpy = models.FloatField(max_length=30, default = None)
