import requests
import json


try:
    #  Gets json data from URL
    USDtoZMW = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=USD_ZMW&compact=y")
    GBPtoZMW = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=GBP_ZMW&compact=y")

    # Loads the Contents of Json retreived from URL
    USDtoZMW = json.loads(USDtoZMW.content)
    GBPtoZMW = json.loads(GBPtoZMW.content)

    # Dumps Json Files to local storage 
    with open ('data.json', 'w') as a, open('data2.json', 'w') as b:
        json.dump(USDtoZMW, a)
        json.dump(GBPtoZMW, b)

except requests.ConnectionError as e:
    print('Could not connect to Network')
    print('Using Offline data')
    print(' ')

    # Loads values from Json files 
    with open('data.json') as a, open('data2.json') as b:
        data = json.load(a)
        data2 = json.load(b)

    USDtoZMW = data["USD_ZMW"]["val"]
    GBPtoZMW = data2["GBP_ZMW"]["val"]
     
else:
    USDtoZMW = USDtoZMW["USD_ZMW"]["val"]
    GBPtoZMW = GBPtoZMW["GBP_ZMW"]["val"]
    










