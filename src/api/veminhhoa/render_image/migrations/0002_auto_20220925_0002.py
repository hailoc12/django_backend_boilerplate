# Generated by Django 3.2.13 on 2022-09-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render_image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendertemplate',
            name='guidance_scale',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rendertemplate',
            name='prompt_strength',
            field=models.FloatField(default=0),
        ),
    ]
