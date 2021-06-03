from django.db import models

from django.db.models.deletion import DO_NOTHING

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    intro = models.CharField(max_length=250,blank=True,null=True)

    page_header=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        related_name='page_header',
        on_delete=models.DO_NOTHING,
    )

    page_footer=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        related_name='page_footer',
        on_delete=models.DO_NOTHING,
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel('page_header'),
        ImageChooserPanel('page_footer'),
        
    ]

