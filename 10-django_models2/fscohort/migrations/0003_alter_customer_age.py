# Generated by Django 4.2.1 on 2023-05-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(blank=True, choices=[(10, 'Yas: 10'), (20, 'Yas: 20'), (30, 'Yas: 30'), (40, 'Yas: 40'), (50, 'Yas: 50')], default=0, null=True),
        ),
    ]
