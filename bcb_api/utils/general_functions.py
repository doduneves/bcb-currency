import json
import re 

from utils import request_functions as rf

def generate_quotes(simbol, quotation_date = ''):
    quotes = {}
    for simbol_quote in rf.get_all_quotations():
        quotes[simbol_quote] = rf.request_bcb_quotation(quotation_date, simbol_quote)

    if simbol in quotes:
        dolar_val = quotes[simbol]

        for quote in quotes.keys():
            new_value = (quotes[quote] / dolar_val) if dolar_val != 0 else 0
            quotes[quote] = new_value

        quotes['BRL'] = 1 / dolar_val if dolar_val != 0 else 0

    return quotes

def get_min_quote(list_quotes):
    min_val = 0
    min_quote = ''

    for quote, val in list_quotes.items():
        if min_val == 0 or val < min_val:
            min_val = val
            min_quote = quote
    
    return min_quote

def get_currency_contry(symbol):
    
    # Dados mockados pois não encontrei na API o país de origem de cada moeda
    with open('country_mock.json') as json_file:
        data = json.load(json_file)
        if symbol in data:
            return data[symbol]['paisOrigem']

    return 'Indefinido'

def format_data_input(input = ''):
    try:
        input = re.findall("\d+", input)[0]
        if len(input) == 8:
            return input[4:6] + "-" + input[6:8] + "-" + input[0:4]
        else:
            print("Invalid input format. Please set in 'YYYYMMDD'")
            Exception("Invalid input format. Please set in 'YYYYMMDD'")
    except:
        print("Invalid input format. Please set in 'YYYYMMDD'")
        raise 
