# Generated by Django 2.1.5 on 2020-01-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaorders', '0007_auto_20200113_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza_types',
            name='size',
        ),
        migrations.AddField(
            model_name='pizza_types',
            name='size',
            field=models.CharField(choices=[('MEDIUM', 'M'), ('LARGE', 'L')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Pizza_Sizes',
        ),
    ]
