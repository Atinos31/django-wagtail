# Generated by Django 3.2 on 2022-07-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0002_alter_genericpage_banner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True),
        ),
    ]
