# Generated by Django 3.2.13 on 2022-05-31 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0010_auto_20220526_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='botsubcriber',
            name='feature_args',
            field=models.JSONField(blank=True, null=True, verbose_name='Tham số'),
        ),
    ]
