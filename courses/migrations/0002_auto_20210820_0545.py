# Generated by Django 3.2.5 on 2021-08-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(default='jane', max_length=30),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_units',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courses',
            name='syllabus',
            field=models.CharField(default='Sincere', max_length=100),
        ),
    ]