# Generated by Django 3.2.5 on 2021-09-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210820_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(blank='true', max_length=30, null='true'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='syllabus',
            field=models.CharField(blank='true', max_length=100, null='true'),
        ),
    ]