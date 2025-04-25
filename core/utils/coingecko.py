import requests

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

#fetch_prices is a function that is built to make api requests.
#it does not use curl, but i mentioned curl to help you understand what request it makes:
#calling this function : 
#fetch_prices(['bitcoin','ethereum'],['usd','eur'])
#is like to use:
# curl --request GET \
#      --url "https://api.coingecko.com/api/v3/simple/price" \
#      --header 'accept: application/json' \
#      --get \
#      --data "ids=bitcoin,ethereum" \
#      --data "vs_currencies=usd,eur" 


def fetch_prices(crypto_ids,vs_currencies):
    """
    Fetches current price data from CoinGecko.

    :param crypto_ids: list of CoinGecko IDs (e.g., ['bitcoin', 'ethereum'])
    :param vs_currencies: list of target currencies (e.g., ['usd', 'eur'])
    :return: dict mapping like {'bitcoin': {'usd': 64500, 'eur': 60000}, ...}
    """
    params = {
        "ids":','.join(crypto_ids),
        "vs_currencies":','.join(vs_currencies),
    }

    try:
        response = requests.get(COINGECKO_API_URL,params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] CoinGecko API call failed : {e}")
        return {}
    


