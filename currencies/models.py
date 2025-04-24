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

    def __str__(self):
        return f"{self.name} ({self.code})"

    