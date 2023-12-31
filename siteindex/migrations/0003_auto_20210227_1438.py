# Generated by Django 3.1.5 on 2021-02-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteindex', '0002_quota_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='parag_2',
            field=models.TextField(blank=True, help_text='正文第二段', max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='parag_3',
            field=models.TextField(blank=True, help_text='正文第三段', max_length=100000, null=True),
        ),
    ]
