from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class HomePage(Page):

    content_panels = Page.content_panels + [FieldPanel("owner")]
