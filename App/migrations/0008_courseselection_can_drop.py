# Generated by Django 4.2 on 2023-04-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_class_remaining_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseselection',
            name='can_drop',
            field=models.BooleanField(default=False),
        ),
    ]
