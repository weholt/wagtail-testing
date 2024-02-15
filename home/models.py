from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import (
    InlinePanel,
    MultiFieldPanel,
)

from wagtail.models import Orderable
from wagtail.models import Page


class HomePage(Page):

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel("non_page2_list", label="Non-page 2"),
            ],
            heading="Other non-page models",
            classname="collapsed",
        ),
    ]


@register_snippet
class NonPage1(Orderable):

    text = models.CharField(max_length=50)
    selected = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "%s (selected: %s)" % (self.text, self.selected)


def query_limiter():
    return {"selected": True}


@register_snippet
class NonPage2(Orderable):

    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name="non_page2_list",
        null=True,
    )
    name = models.CharField(max_length=50)
    non_page1 = models.ForeignKey(
        NonPage1,
        on_delete=models.SET_NULL,
        limit_choices_to=query_limiter,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return "%s - %s" % (self.name, self.non_page1)
