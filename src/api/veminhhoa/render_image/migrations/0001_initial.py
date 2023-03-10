# Generated by Django 3.2.13 on 2022-09-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RenderTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('prompt_template', models.TextField(blank=True)),
                ('num_inference_steps', models.IntegerField(default=0)),
                ('prompt_strength', models.IntegerField(default=0)),
                ('guidance_scale', models.IntegerField(default=0)),
            ],
        ),
    ]
