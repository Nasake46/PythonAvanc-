# Generated by Django 3.2.8 on 2021-10-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wilfridapp', '0002_checkwebsite'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkwebsite',
            name='is_up',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
