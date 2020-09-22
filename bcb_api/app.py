import sys
sys.path.append('/utils/general_functions/')

import fileinput

from utils import general_functions as gf

if __name__ == '__main__':


    for line in fileinput.input():
        input_formatted = gf.format_data_input(line)
            
        list_quotes = gf.generate_quotes('USD', input_formatted)

        currency_symbol = gf.get_min_quote(list_quotes)
        currency_value = list_quotes[currency_symbol]
        currency_country = gf.get_currency_contry(currency_symbol)

        if currency_value:
            print(str(currency_symbol) + ", " + str(currency_value) + ", " + str(currency_country))
        else:
            print("x")


