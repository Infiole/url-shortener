# Generated by Django 3.2.7 on 2021-09-06 03:50

from django.db import migrations, models
import shrinker.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('short_url', models.CharField(default=shrinker.utilities.generate_short_url, max_length=7, primary_key=True, serialize=False)),
                ('long_url', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
