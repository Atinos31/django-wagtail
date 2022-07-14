from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    banner_title = models.CharField(
        max_length=150,
        default='Welcome to AGRINFO!')

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
    ]

