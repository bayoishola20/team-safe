# Generated by Django 2.0.4 on 2018-04-28 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('incidence', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AddField(
            model_name='incidence',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incidence',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
