# Generated by Django 4.2 on 2023-04-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_class_options_remove_class_class_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='remaining_selection',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
