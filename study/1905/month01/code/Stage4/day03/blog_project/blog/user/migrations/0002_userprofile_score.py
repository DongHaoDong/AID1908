# Generated by Django 2.2.6 on 2019-12-16 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='score',
            field=models.IntegerField(default=0, null=True, verbose_name='分数'),
        ),
    ]