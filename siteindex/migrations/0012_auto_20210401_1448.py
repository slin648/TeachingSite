# Generated by Django 3.1.7 on 2021-04-01 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteindex', '0011_lesson_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quota',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='quota',
            name='student',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Quota',
        ),
    ]
