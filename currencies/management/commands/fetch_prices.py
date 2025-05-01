from django.core.management.base import BaseCommand
from currencies.models import Currency
from core.utils.coingecko import fetch_prices
from currencies.services.price_service import save_prices_from_coingecko
class Command(BaseCommand):
    help = "command to fetch currency prices from coingecko"

    def handle(self, *args, **options):
        
        crypto_queryset = Currency.objects.filter(type="CRYPTO").values_list("coingecko_id")
        fiat_queryset = Currency.objects.filter(type="FIAT").values_list("coingecko_id")
        if not crypto_queryset or not fiat_queryset:
            print("[ERROR] database does not contain Crypto / Fiat currency.")
            return 1
        
        crypto_list = [item[0] for item in crypto_queryset]
        del crypto_queryset

        fiat_list = [item[0] for item in fiat_queryset]
        del fiat_queryset

        data=fetch_prices(crypto_ids=crypto_list,vs_currencies=fiat_list)
        if data:
            save_prices_from_coingecko(data)
            print("Prices fetched and saved.")
        else:
            print("Failed to fetch prices.")
            return 1
        