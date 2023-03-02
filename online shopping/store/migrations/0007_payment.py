# Generated by Django 3.1.7 on 2022-11-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atm', models.CharField(max_length=15)),
                ('cvv', models.CharField(max_length=3)),
                ('date', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]