
from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)
from .models import Testimonials

# Register your models here.


@modeladmin_register
class TestimonialAdmin(ModelAdmin):
    """ testimonial admin """
    model = Testimonials
    menu_label = "Testimonials"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_it_from_explored = False
    list_display = ("quote", "attribution")
    search_fields = ("quote", "attribution") #search built in 