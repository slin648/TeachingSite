# Generated by Django 3.1.7 on 2021-04-05 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_auto_20210402_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='result',
            options={'ordering': ['score']},
        ),
    ]