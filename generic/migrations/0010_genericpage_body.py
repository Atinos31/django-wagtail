# Generated by Django 3.2 on 2022-07-14 14:48

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0009_genericpage_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=None),
        ),
    ]