# Generated by Django 3.0.7 on 2020-06-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20200621_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
