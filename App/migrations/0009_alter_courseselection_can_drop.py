# Generated by Django 4.2 on 2023-04-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_courseselection_can_drop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseselection',
            name='can_drop',
            field=models.BooleanField(default=True),
        ),
    ]
