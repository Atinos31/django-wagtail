from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    
    lead_text = models.CharField(
        max_length=500,
        blank=True,
        help_text='Subheader text under the banner title'
    )
    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optiom page to link to',
        on_delete=models.SET_NULL,

    )
    button_text = models.CharField(
        max_length=50,
        default='Read more',
        blank=False,
        help_text='Button Text',
    )
    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='The banner background image',
        on_delete=models.SET_NULL,
    )
   
    content_panels = Page.content_panels + [
        FieldPanel('lead_text'),
        PageChooserPanel("button"),
        FieldPanel('button_text'),
        ImageChooserPanel("banner_background_image"),


    ]
