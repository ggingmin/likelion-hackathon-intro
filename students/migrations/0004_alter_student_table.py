# Generated by Django 4.0.4 on 2022-05-24 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_student_num'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='TB_STUDENTS',
        ),
    ]
