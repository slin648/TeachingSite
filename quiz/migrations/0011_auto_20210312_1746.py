# Generated by Django 3.1.5 on 2021-03-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20210312_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
