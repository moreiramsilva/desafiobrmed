from django import forms
 
#Moedas  
CURRENCY =(
    ("1", "BRL"),
    ("2", "EUR"),
    ("3", "JPY"),
)

#Formulario  
class CurrencyForm(forms.Form):
    currency_field = forms.ChoiceField(choices = CURRENCY)