from django.contrib import admin
from django.db import models
from fluent_pages.pagetypes.flatpage.models import FlatPage

# Note: we are renaming the original Admin and Form as we import them!
from fluent_pages.pagetypes.flatpage.admin import FlatPageAdmin as FlatPageAdminOld
# from fluent_pages.pagetypes.flatpage.admin import FlatpageForm as FlatpageFormOld

from django import forms
from ckeditor.widgets import CKEditorWidget

# class FlatpageForm(FlatpageFormOld):
#     content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = FlatPage # this is not automatically inherited from FlatpageFormOld


class FlatPageAdmin(FlatPageAdminOld):
    # form = FlatpageForm
    change_form_template = "admin/fluent_pages/pagetypes/flatpage/change_form.html"
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)