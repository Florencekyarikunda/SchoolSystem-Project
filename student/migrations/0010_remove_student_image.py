# Generated by Django 3.2.5 on 2021-09-07 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
