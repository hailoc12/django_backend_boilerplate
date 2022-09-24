# Generated by Django 3.2.13 on 2022-09-24 21:01

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('render_image', '0004_auto_20220925_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenderTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_prompt', models.TextField(blank=True)),
                ('translated_prompt', models.TextField(blank=True)),
                ('processed_prompt', models.TextField(blank=True)),
                ('image_urls', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), size=None)),
                ('estimated_price', models.FloatField(default=0)),
                ('final_price', models.FloatField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status_code', models.IntegerField(default=0)),
                ('retry_count', models.IntegerField(default=5)),
                ('user_review', models.IntegerField(default=0)),
                ('user_feedback', models.TextField(blank=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
