from django.utils import timezone
from currencies.models import Currency,Price
from decimal import Decimal
def save_prices_from_coingecko(data,source="coingecko"):
    """
    Save fetched price data into the database.

    :param data: dict from fetch_prices(), example:
                 {'bitcoin': {'usd': 64500.0, 'eur': 60000.0}}
    :param source: string indicating where the data came from
    """
    now = timezone.now()

    for crypto_id,vs_currencies_dict in data.items():
        try:
            base_currency = Currency.objects.get(coingecko_id = crypto_id)
        except Currency.DoesNotExist:
            print(f"[WARNING] Base currency with coingecko_id '{crypto_id}' not found.")
            continue
        for vs_currency_key, rate in vs_currencies_dict.items():
            try:
                quote_currency = Currency.objects.get(coingecko_id = vs_currency_key)
            except Currency.DoesNotExist:
                print(f"[WARNING] Quote currency '{vs_currency_key}' not found in database.")
                continue
            Price.objects.create(
                base_currency=base_currency,
                quote_currency=quote_currency,
                rate=Decimal(str(rate)),
                timestamp=now,
                source=source
            )
