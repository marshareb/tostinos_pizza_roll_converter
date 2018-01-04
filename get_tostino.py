from tkinter import *
import urllib.request
import pip

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # LABEL AND ENTRY FIELD
        self.text_label = Label(self, text = "Enter amount:")
        self.text_label.grid(row = 0, column = 0, columnspan = 3)
        self.text_entry = Entry(self, width = 20)
        self.text_entry.grid(row = 1, column = 0, columnspan = 3)

        # CURRENCY CHOICES
        self.currency = StringVar()
        self.currency.set(None)
        self.currency_label = Label(self, text = "Choose your currency:")
        self.currency_label.grid(row = 2, column = 0, columnspan = 6)
        self.dollar_button = Radiobutton(self, text = "US Dollar", variable = self.currency, value = 'USD')
        self.dollar_button.grid(row = 3, column = 0)
        self.peso_button = Radiobutton(self, text = "Peso", variable = self.currency, value = "MXN")
        self.peso_button.grid(row = 3, column = 1)
        self.rupee_button = Radiobutton(self, text = "Rupee", variable = self.currency, value = "INR")
        self.rupee_button.grid(row = 3, column = 2)
        self.euro_button = Radiobutton(self, text = "Euro", variable = self.currency, value = "EUR")
        self.euro_button.grid(row = 4, column = 0)
        self.pound_button = Radiobutton(self, text = "Pound", variable = self.currency, value = "GBP")
        self.pound_button.grid(row = 4, column = 1)
        self.yen_button = Radiobutton(self, text = "Yen", variable = self.currency, value = "JPY")
        self.yen_button.grid(row = 4, column = 2)

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

# main
root = Tk()
root.title("Caesar Cypher")
root.geometry("200x300")
root.resizable(width = FALSE, height = FALSE)
app = Application(root)
root.mainloop()