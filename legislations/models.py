from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from wagtail.fields import RichTextField
from datetime import datetime, date
from django.utils.timezone import timezone
# Create your models here.

class LegislationListingPage(Page):
    """ Render legislation listing page"""
    template = 'legislations/legislation_listing_page.html'
    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['legislations'] = LegislationPage.objects.live().public()# ORM
        # space_comapny = 'x'
        # import pudb; pu.db()
        return context

class LegislationPage(Page):
    """ Render legislation page"""

    template = 'legislations/legislation_page.html'
    description = RichTextField(blank=True)
    country = CountryField(
        blank_label='(select country)',
        null=False,
        blank=False)
    countries = CountryField(multiple=True)
    date_issued = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    date_into_practice = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an internal wagtail page',
        on_delete=models.SET_NULL
    )
    external_page = models.URLField(blank=True)
    button_text = models.CharField(blank=True, max_length=50)
    legislation_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='This image will be used on the service Listing page and will be cropped to 570px by 370px on this page',
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        PageChooserPanel('internal_page'),
        PageChooserPanel('country'),
        PageChooserPanel('countries'),
        FieldPanel('date_issued'),
        FieldPanel('date_into_practice'),
        FieldPanel('external_page'),
        FieldPanel('button_text'),
        ImageChooserPanel('legislation_image')
    ]

# validations
    def clean(self):
        super().clean()
    
        if self.internal_page and self.external_page:
            # both fields are filled out
            raise ValidationError({
                'internal_page': ValidationError("Please only select a page OR enter an external URL"),
                'external_page': ValidationError("Oupppssssssss Please only select a page OR enter an external URL"),
            })

        if not self.internal_page and not self.external_page:
            raise ValidationError({
                'internal_page': ValidationError("You must always select a page OR enter an external URL"),
                'external_page': ValidationError("You must always select a page OR enter an external URL"),
            })
    #    if something:
    #     cause an error