# Generated by Django 3.1.5 on 2021-02-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteindex', '0003_auto_20210227_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='intro',
            field=models.TextField(blank=True, help_text='讲师简介', max_length=10000, null=True),
        ),
    ]