# Generated by Django 4.2 on 2023-04-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_courseselection_can_drop'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='class',
            name='start',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='time',
            field=models.CharField(choices=[(1, '一'), (2, '二'), (3, '三'), (4, '四'), (5, '五')], default=1, max_length=10),
        ),
    ]
