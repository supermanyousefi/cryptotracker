from django.db import models

# Create your models here.
class Currency(models.Model):
    class CurrencyType(models.TextChoices):
        FIAT = "FIAT","Fiat Currency"
        CRYPTO = "CRYPTO","Cryptocurrency"

    code    = models.CharField(max_length=10,unique=True) # BTC,USD,CAD ...
    name    = models.CharField(max_length=100)           # Bitcoin, US dollar, Canada dollar ...
    type    = models.CharField(max_length=10,choices=CurrencyType.choices)
    symbol  = models.CharField(max_length=10,blank=True,null=True) # $ or ₿ but it's optional.
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Currencies'
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Price(models.Model):
    base_currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='base_prices')
    quote_currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='quote_prices')
    rate = models.DecimalField(max_digits = 20,decimal_places = 10)
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=100,blank=True,null=True)
    
    class Meta:
        unique_together = ('base_currency','quote_currency','timestamp')
        ordering = ["-timestamp"]
    
    def __str__(self):
        return f"{self.base_currency.code}/{self.quote_currency.code} @ {self.rate} on {self.timestamp}"
    