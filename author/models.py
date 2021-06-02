from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

# Create your models here.
class AuthorPage(Page):
    intro = models.CharField(max_length=250)
    author_pic=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel('author_pic')
    ]
