# Generated by Django 3.1.7 on 2021-04-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteindex', '0020_auto_20210405_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
