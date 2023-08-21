# Generated by Django 3.1.7 on 2021-04-05 10:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('siteindex', '0019_delete_lessoncomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='该课程的唯一ID', primary_key=True, serialize=False),
        ),
    ]