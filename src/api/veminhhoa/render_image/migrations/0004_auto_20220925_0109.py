# Generated by Django 3.2.13 on 2022-09-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('render_image', '0003_auto_20220925_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendertemplate',
            name='improve_face',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rendertemplate',
            name='price',
            field=models.FloatField(default=1.0),
        ),
    ]