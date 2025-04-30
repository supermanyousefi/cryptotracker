# populate_currencies.py
from django.core.management.base import BaseCommand
from currencies.models import Currency  # Replace 'your_app' with your actual app name

class Command(BaseCommand):
    help = 'Populates the database with initial currency data'

    def handle(self, *args, **options):
        currencies = [
            # Fiat Currencies
            {
                'code': 'USD',
                'name': 'US Dollar',
                'type': Currency.CurrencyType.FIAT,
                'symbol': '$',
                'coingecko_id': 'usd'
            },
            {
                'code': 'EUR',
                'name': 'Euro',
                'type': Currency.CurrencyType.FIAT,
                'symbol': '€',
                'coingecko_id': 'eur'
            },
            {
                'code': 'GBP',
                'name': 'British Pound',
                'type': Currency.CurrencyType.FIAT,
                'symbol': '£',
                'coingecko_id': 'gbp'
            },
            {
                'code': 'JPY',
                'name': 'Japanese Yen',
                'type': Currency.CurrencyType.FIAT,
                'symbol': '¥',
                'coingecko_id': 'jpy'
            },
            {
                'code': 'CAD',
                'name': 'Canadian Dollar',
                'type': Currency.CurrencyType.FIAT,
                'symbol': '$',
                'coingecko_id': 'cad'
            },
            {
                'code': 'AUD',
                'name': 'Australian Dollar',
                'type': Currency.CurrencyType.FIAT,
                'symbol': '$',
                'coingecko_id': 'aud'
            },
            {
                'code': 'CNY',
                'name': 'Chinese Yuan',
                'type': Currency.CurrencyType.FIAT,
                'symbol': '¥',
                'coingecko_id': 'cny'
            },
            
            # Cryptocurrencies
            {
                'code': 'BTC',
                'name': 'Bitcoin',
                'type': Currency.CurrencyType.CRYPTO,
                'symbol': '₿',
                'coingecko_id': 'bitcoin'
            },
            {
                'code': 'ETH',
                'name': 'Ethereum',
                'type': Currency.CurrencyType.CRYPTO,
                'symbol': 'Ξ',
                'coingecko_id': 'ethereum'
            },
            {
                'code': 'BNB',
                'name': 'Binance Coin',
                'type': Currency.CurrencyType.CRYPTO,
                'symbol': '',
                'coingecko_id': 'binancecoin'
            },
            {
                'code': 'XRP',
                'name': 'Ripple',
                'type': Currency.CurrencyType.CRYPTO,
                'symbol': '',
                'coingecko_id': 'ripple'
            },
            {
                'code': 'SOL',
                'name': 'Solana',
                'type': Currency.CurrencyType.CRYPTO,
                'symbol': '',
                'coingecko_id': 'solana'
            },
            {
                'code': 'ADA',
                'name': 'Cardano',
                'type': Currency.CurrencyType.CRYPTO,
                'symbol': '',
                'coingecko_id': 'cardano'
            },
            {
                'code': 'DOGE',
                'name': 'Dogecoin',
                'type': Currency.CurrencyType.CRYPTO,
                'symbol': 'Ð',
                'coingecko_id': 'dogecoin'
            },
        ]

        created_count = 0
        for currency_data in currencies:
            _, created = Currency.objects.get_or_create(
                code=currency_data['code'],
                defaults=currency_data
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {created_count} currencies'))