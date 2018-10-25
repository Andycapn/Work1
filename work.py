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

        Query2 = input("Enter the Currency You're Converting from ")

        if Query2 == 'K':
            Currency1 = float(input('Enter the amount in K: '))
            Cur1 = Currency1
            Currency1 = Currency1 / USDtoZMW
            Currency1a = Cur1 / GBPtoZMW
            Currency1 = float(round(Currency1, 2))
            Currency1a = float(round(Currency1a, 2))
            print('$', Currency1)
            print('GBP', Currency1a)

        if Query2 == '$':
            Currency2 = float(input('Enter the amount in $: '))
            Currency2 = Currency2 * USDtoZMW
            Currency2 = float(round(Currency2, 2))
            print('K', Currency2)

        if Query2 == 'GBP':
            Currency3 = float(input('Enter the amount in GBP: '))
            Currency3 = Currency3 * GBPtoZMW
            Currency3 = float(round(Currency3, 2))
            print('K', Currency3)

        if Query2 == 'all':
            CurrencyAll = float(input('Enter the Amount'))





# def CurrencyConvertor(Currency, USDtoZMW, GBPtoZMW):
#     Currency = float(input('Enter the amount '))   

    





