# pip install forex-python
from forex_python.converter import CurrencyRates
c = CurrencyRates()

print("Введите наименование валюты (поддерживаются только USD, EUR, RUB :( )):")

currency = input()

print(c.get_rates(currency))