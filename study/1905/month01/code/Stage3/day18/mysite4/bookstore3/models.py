from django.db import models

# Create your models here.


class Author3(models.Model):
    name = models.CharField(max_length=50,verbose_name="姓名")
    def __str__(self):
        return "作家:"+self.name

class Book3(models.Model):
    title = models.CharField(max_length=50,verbose_name="书名")
    authors = models.ManyToManyField(Author3)
    def __str__(self):
        return "图书："+self.title