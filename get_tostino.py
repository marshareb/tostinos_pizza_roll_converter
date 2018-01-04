import urllib.request
import pip

def get_pizza_roll():
    f = urllib.request.urlopen("https://www.amazon.com/Totinos-Pepperoni-Pizza-Rolls-Ounce/dp/B00PJ8MPD8/"
                               "ref=sr_1_2_a_it?ie=UTF8&qid=1515024359&sr=8-2&keywords=totino%27s%20pizza%20rolls")
    x=str(f.read()).split("<")
    j =''
    for i in x:
        if 'priceblock_ourprice" class="a-size-medium a-color-price"' in i:
            j = i
            break
    # 6 * 90 = 450 pizza rolls
    return(round(float(j[-5:])/450, 2))


def convert_currency(currency1, currency2):
    try:
        from currency_converter import CurrencyConverter
    except:
        pip.main(['install', 'currencyconverter'])
        from currency_converter import CurrencyConverter
    if currency1 == 'TOT':
        if currency2 == 'USD':
            return round((get_pizza_roll()),2)
        else:
            x = (get_pizza_roll())
            y = float(CurrencyConverter().convert(1, 'USD', currency2))
            return round(float(x * y),2)
    if currency2 == 'TOT':
        if currency1 == 'USD':
            return 1/(get_pizza_roll())
        else:
            x = 1/(get_pizza_roll())
            y = float(CurrencyConverter().convert(1, currency1, 'USD'))
            return round(float(x * y),2)
    return(round(CurrencyConverter().convert(1, currency1, currency2),2))

def converter(amount, currency):
    return(round(convert_currency(currency, 'TOT') * amount))

if __name__ == '__main__':
    #TEST
    print(converter(1, 'EUR'))