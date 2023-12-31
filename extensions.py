import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(self, quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Неудалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Неудалось обработать количество {amount}.')

        quote_ticker, base_ticker = keys[quote], keys[base]
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

        total_base = json.loads(r.content)[base_ticker]
        return total_base
