# Generated by Django 3.1.5 on 2021-03-13 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteindex', '0010_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
    ]
