# Generated by Django 4.1.5 on 2023-04-12 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_alter_meal_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
