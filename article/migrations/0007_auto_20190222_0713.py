# Generated by Django 2.1.7 on 2019-02-22 07:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20190222_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('carousel', wagtail.core.blocks.StreamBlock([('image', wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('caption_header', wagtail.core.blocks.CharBlock(required=False)), ('caption_text', wagtail.core.blocks.TextBlock(required=False))])), ('video', wagtail.embeds.blocks.EmbedBlock())], block_counts={'video': {'max_num': 2}}, max_num=10))]),
        ),
    ]
