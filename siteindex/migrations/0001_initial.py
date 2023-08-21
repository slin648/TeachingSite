# Generated by Django 3.1.5 on 2021-02-26 07:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='输入该节课程的简介', max_length=1000)),
                ('date_of_release', models.DateField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='images')),
                ('parag_1', models.TextField(help_text='正文第一段', max_length=100000, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images')),
                ('parag_2', models.TextField(help_text='正文第二段', max_length=100000, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='images')),
                ('parag_3', models.TextField(help_text='正文第三段', max_length=100000, null=True)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteindex.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='输入一个主题(例如"计算机硬件")', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='该名额的唯一ID', primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('a', '未学习'), ('b', '学习中'), ('c', '已学习')], default='a', help_text='学习情况', max_length=1)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='siteindex.lesson')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='topic',
            field=models.ManyToManyField(help_text='选择该节课程涵盖的主题', to='siteindex.Topic'),
        ),
    ]
