# Generated by Django 3.2.13 on 2022-05-18 08:57

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kq_xo_so', '0012_auto_20220518_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau0',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default=[], verbose_name='Đầu lô tô đầu 0'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau1',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default=[], verbose_name='Đầu lô tô đầu 1'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau2',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default=[], verbose_name='Đầu lô tô đầu 2'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau3',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default=[], verbose_name='Đầu lô tô đầu 3'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau4',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default=[], verbose_name='Đầu lô tô đầu 4'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau5',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default=[], verbose_name='Đầu lô tô đầu 5'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau6',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đầu lô tô đầu 6'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau7',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đầu lô tô đầu 7'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau8',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đầu lô tô đầu 8'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to_dau9',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đầu lô tô đầu 9'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau0',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 0'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau1',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 1'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau2',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 2'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau3',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 3'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau4',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 4'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau5',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 5'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau6',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 6'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau7',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 7'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau8',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 8'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to_dau9',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô đầu 9'), null=True, size=None),
        ),
    ]
