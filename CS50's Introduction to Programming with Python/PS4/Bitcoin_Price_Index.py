# Bitcoin Price Index
import sys
import json
import requests


try:
    buy = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    print(f"$ {buy*o["bpi"]["USD"]["rate_float"]}")
except Exception as e:
    sys.exit(f"An error occurred: {e}")