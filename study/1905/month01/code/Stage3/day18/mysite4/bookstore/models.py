from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=30,null=False,unique=True,verbose_name="书名")     # varchar(30)
    pub = models.CharField(max_length=50,null=True,verbose_name="出版社")
    price = models.DecimalField(decimal_places=2,max_digits=7,verbose_name="定价",default=88888,)      # Decimal(7,2)
    market_price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name="零售价",default=99999)


    def __str__(self):
        return "书名:%s,出版社:%s,定价:%s,零售价:%s"%(self.title,self.pub,self.price,self.market_price)


class Author(models.Model):
    name = models.CharField(max_length=30,null=False,verbose_name="作者")
    age = models.IntegerField(verbose_name="年龄",default=1)
    email = models.EmailField(verbose_name="邮箱",default='123@163.com')
    def __str__(self):
        return "作者:%s,年龄:%s,邮箱:%s"%(self.name,self.age,self.email)


class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    author = models.OneToOneField(Author,on_delete=models.CASCADE)


