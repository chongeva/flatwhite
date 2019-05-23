from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.search import index

from core.models import CarouselBlock


class ArticleIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        articlepages = self.get_children().live()
        # articlepages = self.get_children().live().order_by('-first_published_at')
        context['articlepages'] = articlepages
        return context


class ArticlePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    # body = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('carousel', CarouselBlock(max_num=10, block_counts={'video': {'max_num': 2}})),
        ('table', TableBlock(template='includes/table.html'))
    ], blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        # FieldPanel('body', classname="full"),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None


class ArticlePageGalleryImage(Orderable):
    page = ParentalKey(ArticlePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


'''=== Signals ==='''
from django.db.models.signals import pre_delete, post_save
# from django.dispatch import receiver
# from django.contrib.admin.models import LogEntry
from core.logger import log_addition_with_msg, log_deletion, log_change

# @receiver(post_save, sender=ArticlePage)
def post_save_articlepage(sender, instance, created, **kwargs):
    # print(instance)
    if created:
        # latest_revision = instance.get_latest_revision()
        log_addition_with_msg(None, instance, user_id=instance.owner.id)
    else:
        latest_revision = instance.get_latest_revision()
        # print(latest_revision)
        # print(latest_revision.user)
        log_change(None, instance, "Changed Page Content", user_id=latest_revision.user.id)


# @receiver(pre_delete, sender=ArticlePage)
def pre_delete_articlepage(sender, instance, **kwargs):
    latest_revision = instance.get_latest_revision()
    log_deletion(None, instance, "Deleted Page", user_id=latest_revision.user.id)


post_save.connect(post_save_articlepage, sender=ArticleIndexPage)
post_save.connect(post_save_articlepage, sender=ArticlePage)

pre_delete.connect(pre_delete_articlepage, sender=ArticleIndexPage)
pre_delete.connect(pre_delete_articlepage, sender=ArticlePage)
