from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from django.contrib.admin.models import LogEntry


class LogEntryAdmin(ModelAdmin):
    model = LogEntry
    menu_label = 'Log Entries'  # ditch this to use verbose_name_plural from model
    menu_icon = 'list-ul'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = True  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('user', 'action_flag', 'object_repr', 'change_message', 'action_time')
    list_filter = ('user', 'action_flag',)


# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(LogEntryAdmin)
