# Generated by Django 2.0.6 on 2018-07-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180628_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='anonymous', max_length=30),
        ),
    ]
