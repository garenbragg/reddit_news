# Generated by Django 3.0.7 on 2020-06-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200628_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoilerHeadline',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PUHeadline',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('url', models.TextField()),
            ],
        ),
    ]
