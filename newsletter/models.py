from django.db import models
from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

class Newsletter(Campaign):
    headline = models.CharField(
        max_length=500,
        help_text="The headline to use for newsletter."
    )
    header_background = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="The image to udr for the header background.",
        on_delete=models.SET_NULL,
        )
    body = StreamField(DefaultBlocks())
    panels = Campaign.panels + [
            FieldPanel("headline"),
            ImageChooserPanel("header_background"),
            StreamFieldPanel("body"),
    ]

