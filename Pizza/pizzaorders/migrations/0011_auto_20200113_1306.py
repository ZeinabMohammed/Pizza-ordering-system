# Generated by Django 2.1.5 on 2020-01-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaorders', '0010_auto_20200113_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pizzas_size',
        ),
        migrations.AddField(
            model_name='pizza_types',
            name='price',
            field=models.DecimalField(decimal_places=2, default=39.99, max_digits=20),
        ),
        migrations.AddField(
            model_name='pizza_types',
            name='size',
            field=models.CharField(choices=[('MEDIUM', 'M'), ('LARGE', 'L')], max_length=10, null=True),
        ),
    ]