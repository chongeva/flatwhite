from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from core.logger import log_addition_with_msg, log_deletion, log_change
from .models import ArticlePage


# @receiver(post_save, sender=ArticlePage)
def post_save_articlepage(sender, instance, created, **kwargs):
    print(instance)
    if created:
        latest_revision = instance.get_latest_revision()
        log_addition_with_msg({"user": latest_revision.user}, instance)
    else:
        latest_revision = instance.get_latest_revision()
        log_change({"user": latest_revision.user}, instance, "Changed Page Content")


@receiver(pre_delete, sender=ArticlePage)
def pre_delete_articlepage(sender, instance, using):
    latest_revision = instance.get_latest_revision()
    log_deletion({"user": latest_revision.user}, instance, "Deleted Page")


post_save.connect(post_save_articlepage)
