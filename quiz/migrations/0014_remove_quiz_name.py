# Generated by Django 3.1.7 on 2021-04-02 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_auto_20210402_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='name',
        ),
    ]