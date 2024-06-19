# Generated by Django 3.2.6 on 2022-08-21 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20220818_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='applicationsetting',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='tenantuser',
            name='created_by',
        ),
        migrations.AddField(
            model_name='address',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applicationsetting',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tenant',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tenantuser',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
