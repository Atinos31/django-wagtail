# Generated by Django 3.2 on 2022-07-14 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0012_uploadeddocument'),
        ('generic', '0005_customdocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='leg_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document'),
        ),
        migrations.DeleteModel(
            name='CustomDocument',
        ),
    ]