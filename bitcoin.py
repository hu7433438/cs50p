import sys
import requests

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    print(f"${n * r.json()['bpi']['USD']['rate_float']:,.4f}")
except requests.RequestException:
    pass
