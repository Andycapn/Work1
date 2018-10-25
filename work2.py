import requests
import json

# Gets USD to ZMW Rate
USDtoZMW = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=USD_ZMW&compact=y")
USDtoZMW = json.loads(USDtoZMW.content)
USDtoZMW = USDtoZMW ["USD_ZMW"]["val"]

# Gets GBP to ZMW rate
GBPtoZMW = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=GBP_ZMW&compact=y")
GBPtoZMW = json.loads(GBPtoZMW.content)
GBPtoZMW = GBPtoZMW["GBP_ZMW"]["val"]




