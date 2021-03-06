# Generated by Django 3.0.7 on 2020-06-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20200630_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
