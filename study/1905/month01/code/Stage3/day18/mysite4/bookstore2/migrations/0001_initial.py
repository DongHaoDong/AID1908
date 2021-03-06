# Generated by Django 2.2.6 on 2019-12-06 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='出版社')),
            ],
        ),
        migrations.CreateModel(
            name='Book2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='书名')),
                ('pub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore2.Publisher')),
            ],
        ),
    ]
