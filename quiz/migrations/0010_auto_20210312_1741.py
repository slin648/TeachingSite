# Generated by Django 3.1.5 on 2021-03-12 09:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_quiz_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='该测验的唯一ID', primary_key=True, serialize=False),
        ),
    ]
