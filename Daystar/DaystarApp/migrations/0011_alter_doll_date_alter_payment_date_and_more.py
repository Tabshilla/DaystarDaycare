# Generated by Django 4.2.13 on 2024-05-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DaystarApp', '0010_alter_doll_date_alter_salesrecord_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doll',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salesrecord',
            name='sale_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
