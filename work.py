total = 0.0
Counter = 0
Query = None
while Query != 'exit()':
    Query = input('Which Program Do you Require ')

    if Query == 'Calculation':
        numberofitems = int(input('Enter The Number Of Items '))
        for i in range (0, numberofitems):
            Counter = Counter + 1
            print('Items ', Counter)
            PriceOfitem = float(input('Enter price of Item K'))
            total = total + PriceOfitem
        print('K ', total)

    if Query == 'Percentage':
        Amount = float(input('Enter Amount K'))
        Percentage = float(input('Enter Percentage '))
        Percentage = Percentage/100

        def percentage (Amount, Percentage):
            percentage = Amount * Percentage
            percentage = float(round(percentage, 2))

            return percentage
        print('K ', percentage(Amount, Percentage))

    if Query == 'Currency':
        from work2 import USDtoZMW, GBPtoZMW

        def CurrencyConvertor(Currency, ExRate):
            Currency = Currency /  ExRate
            Currency = float(round(Currency, 2))

            return Currency

        def CurrencyConvertorB(Currency, ExRate):
            Currency = Currency *  ExRate
            Currency = float(round(Currency, 2))

            return Currency

        Query2 = input("Enter the Currency You're Converting from ")

        if Query2 == 'K':
            ExRate = USDtoZMW
            Currency = float(input('Enter Amount in Kwacha '))

            print('$ ', CurrencyConvertor(Currency, ExRate))

            ExRate = GBPtoZMW

            print('£ ', CurrencyConvertor(Currency, ExRate))
            

        if Query2 == '$':
            ExRate = USDtoZMW
            Currency = float(input('Enter Amount in Dollars '))

            print('K ', CurrencyConvertorB(Currency, ExRate))


        if Query2 == 'GBP':
            ExRate = GBPtoZMW
            Currency = float(input('Enter Amount in £'))

            print('K ', CurrencyConvertorB(Currency, ExRate))
            

        if Query2 == 'all':
            CurrencyAll = float(input('Enter the Amount'))






  

    





