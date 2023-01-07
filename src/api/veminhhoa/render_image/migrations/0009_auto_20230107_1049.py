# Generated by Django 3.2.13 on 2023-01-07 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('render_image', '0008_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='author',
            name='year_of_born',
            field=models.IntegerField(default=1990),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render_image.book')),
            ],
        ),
    ]
