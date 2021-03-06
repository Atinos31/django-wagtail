# Generated by Django 3.2 on 2022-07-15 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('home', '0004_alter_homepage_banner_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_background_image',
            field=models.ForeignKey(help_text='The banner background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button',
            field=models.ForeignKey(blank=True, help_text='Select an optiom page to link to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_text',
            field=models.CharField(default='Read more', help_text='Button Text', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='Subheader text under the banner title', max_length=500),
        ),
    ]
