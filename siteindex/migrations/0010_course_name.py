# Generated by Django 3.1.5 on 2021-03-13 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteindex', '0009_auto_20210313_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
