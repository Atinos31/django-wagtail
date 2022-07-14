from django.db import models
from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel



class GenericPage(Page):
    banner_title = models.CharField(
        max_length=150,
        default='Welcome to my generic page!'
    )
    introduction = models.TextField(
        blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,blank=False,
        on_delete=models.SET_NULL,
        related_name='+')
    author = models.ForeignKey(
        'Author',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',

    )
    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('introduction'),
        ImageChooserPanel('banner_image'),
        SnippetChooserPanel("author"),
   
    ]

# standard django model
@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(blank=True, max_length=100)
    company_name = models.CharField(blank=True, max_length=100)
    company_url = models.URLField(blank=True, max_length=100)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )
    panels = [
        FieldPanel("name"),
        FieldPanel("title"),
        FieldPanel("company_name"),
        FieldPanel("company_url"),
        ImageChooserPanel("image"),

    ]

    def __str__(self):
        return self.name

      