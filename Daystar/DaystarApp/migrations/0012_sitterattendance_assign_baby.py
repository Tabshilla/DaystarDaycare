# Generated by Django 4.2.13 on 2024-05-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DaystarApp', '0011_alter_doll_date_alter_payment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitterattendance',
            name='assign_baby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DaystarApp.babyreg'),
        ),
    ]
