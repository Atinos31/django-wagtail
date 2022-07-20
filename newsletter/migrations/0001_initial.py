# Generated by Django 3.2 on 2022-07-20 10:16

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('birdsong', '0006_auto_20220428_0558'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('campaign_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birdsong.campaign')),
                ('headline', models.CharField(help_text='The headline to use for newsletter.', max_length=500)),
                ('body', wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock(features=['h3', 'h4', 'bold', 'italic', 'link', 'ul', 'ol', 'document-link'], template='birdsong/mail/blocks/richtext.html'))], use_json_field=None)),
                ('header_background', models.ForeignKey(help_text='The image to udr for the header background.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            bases=('birdsong.campaign',),
        ),
    ]