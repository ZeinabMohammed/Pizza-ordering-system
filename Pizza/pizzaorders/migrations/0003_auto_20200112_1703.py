# Generated by Django 2.1.5 on 2020-01-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaorders', '0002_auto_20200112_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza_types',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]