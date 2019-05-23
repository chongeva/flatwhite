from django.db import models

from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class CoverSectionBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    image_position = blocks.ChoiceBlock(choices=[
                    ('left top', 'Left Top'),
                    ('left center', 'Left Center'),
                    ('left bottom', 'Left Bottom'),
                    ('right top', 'Right Top'),
                    ('right center', 'Right Center'),
                    ('right bottom', 'Right Bottom'),
                    ('center top', 'Center Top'),
                    ('center center', 'Center Center'),
                    ('center bottom', 'Center Bottom'),
                ], icon='edit', required=False)
    image_size = blocks.ChoiceBlock(choices=[
                    ('cover', 'Full Cover'),
                    ('half', 'Half'),
                ], icon='edit', required=False)
    background_colour = blocks.CharBlock(required=False)
    description = blocks.RichTextBlock()
    text_align = blocks.ChoiceBlock(choices=[
                    ('left', 'Left'),
                    ('center', 'Center'),
                    ('right', 'Right'),
                ], icon='edit')

    class Meta:
        icon = 'placeholder'


class TextSectionBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    image_position = blocks.ChoiceBlock(choices=[
                    ('left top', 'Left Top'),
                    ('left center', 'Left Center'),
                    ('left bottom', 'Left Bottom'),
                    ('right top', 'Right Top'),
                    ('right center', 'Right Center'),
                    ('right bottom', 'Right Bottom'),
                    ('center top', 'Center Top'),
                    ('center center', 'Center Center'),
                    ('center bottom', 'Center Bottom'),
                ], icon='edit', required=False)
    image_display = blocks.ChoiceBlock(choices=[
                    ('left', 'Left'),
                    ('right', 'Right'),
                    ('background', 'Background'),
                ], icon='edit', required=False)
    background_colour = blocks.CharBlock(required=False)
    description = blocks.RichTextBlock()
    text_align = blocks.ChoiceBlock(choices=[
                    ('left', 'Left'),
                    ('center', 'Center'),
                    ('right', 'Right'),
                ], icon='edit')

    class Meta:
        icon = 'placeholder'


class CarouselImageBlock(blocks.StructBlock):
    photo = ImageChooserBlock()
    caption_header = blocks.CharBlock(required=False)
    caption_text = blocks.TextBlock(required=False)

    class Meta:
        icon = 'picture'


class CarouselBlock(blocks.StreamBlock):
    image = CarouselImageBlock()
    video = EmbedBlock()

    class Meta:
        icon = 'cogs'


class CardItemBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    description = blocks.RichTextBlock()
    text_align = blocks.ChoiceBlock(choices=[
                    ('left', 'Left'),
                    ('center', 'Center'),
                    ('right', 'Right'),
                ], icon='edit')

    class Meta:
        icon = 'picture'


class CardBlock(blocks.StreamBlock):
    card = CardItemBlock()

    class Meta:
        icon = 'picture'
