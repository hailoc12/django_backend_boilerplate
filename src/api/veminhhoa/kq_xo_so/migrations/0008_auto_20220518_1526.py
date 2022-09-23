# Generated by Django 3.2.13 on 2022-05-18 08:26

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kq_xo_so', '0007_auto_20220518_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xosomienbac',
            name='dau_lo_to',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đầu lô tô'), size=None), size=10),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='duoi_lo_to',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Đuôi lô tô'), size=None), size=10),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_ba',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải ba'), size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_bay',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải bảy'), size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_dac_biet',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải đặc biệt'), size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_nam',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải năm'), size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_nhat',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải nhất'), size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_nhi',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải nhì'), size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_sau',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải sáu'), size=None),
        ),
        migrations.AlterField(
            model_name='xosomienbac',
            name='giai_tu',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TextField(blank=True, default='', verbose_name='Giải tư'), size=None),
        ),
    ]
