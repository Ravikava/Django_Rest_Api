# Generated by Django 3.2.10 on 2022-07-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0003_alter_employee_emp_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_mobile',
            field=models.CharField(max_length=10),
        ),
    ]
