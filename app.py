import requests
import json

def get_all_quotations():
    simbols_arr = []
    try:

        resp = requests.get('https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=1000&$format=json&$select=simbolo')
        if resp.status_code == 200:
            str_values = json.dumps(resp.json()['value'])
            values = json.loads(str_values)

            for v in values:
                simbols_arr.append(v['simbolo'])
    except:
        print("Something's wrong in the BCB request")
        raise

    return simbols_arr

def request_bcb_quotation(quotation_date, simbol):
    min_quote = 0

    try:
        url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='" + simbol + "'&@dataCotacao='" + quotation_date +"'&$top=100&$format=json&$select=cotacaoCompra"

        resp = requests.get(url)
        if resp.status_code == 200:
            str_values = json.dumps(resp.json()['value'])
            values = json.loads(str_values)

            for v in values:

                if min_quote == 0 or int(v['cotacaoCompra']) < min_quote:
                    min_quote = v['cotacaoCompra']

    except:
        print("Something's wrong in the BCB request")
        raise
    
    return min_quote



def generate_quotes(simbol, quotation_date = ''):
    quotes = {}
    for simbol_quote in get_all_quotations():
        quotes[simbol_quote] = request_bcb_quotation(quotation_date, simbol_quote)

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

if __name__ == '__main__':
    list_quotes = generate_quotes('USD', '09-01-2020')

    print(get_min_quote(list_quotes))


