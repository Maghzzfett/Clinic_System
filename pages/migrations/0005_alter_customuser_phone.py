# Generated by Django 5.1.2 on 2024-10-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_customuser_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='phone', max_length=30),
        ),
    ]