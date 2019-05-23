from django.db import models
from django.utils.translation import ugettext_lazy as _


class SEOItem(models.Model):
    item_type = models.CharField(_("Type"), max_length=500)
    value = models.CharField(_("Value"), max_length=500)
