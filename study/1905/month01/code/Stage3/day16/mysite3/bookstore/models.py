from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=30,db_index=True)     # varchar(30)
    price = models.DecimalField(decimal_places=2,max_digits=7)      # Decimal(7,2)





