from django.db import models
from django.db.models.deletion import DO_NOTHING

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from author.models import AuthorPage

# Create your models here.
class ArticleIndexPage(Page):
    intro=RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class ArticlePage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    author_info = models.ForeignKey(AuthorPage,blank=True,null=True,related_name='author_info',on_delete=DO_NOTHING)
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('author_info'),
        FieldPanel('body', classname="full"),
    ]


