from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from core.models import CarouselBlock, TextSectionBlock, CoverSectionBlock, CardBlock
# from core.models import CarouselBlock


class HomePage(Page):
    # body = RichTextField(blank=True)
    body = StreamField([
        ('cover', CoverSectionBlock()),
        ('text_section', TextSectionBlock()),
        ('image', ImageChooserBlock()),
        ('card', CardBlock()),
        ('carousel', CarouselBlock(max_num=10, block_counts={'video': {'max_num': 2}})),
    ], null=True)

    content_panels = Page.content_panels + [
        # FieldPanel('body', classname="full"),
        StreamFieldPanel('body'),
    ]
