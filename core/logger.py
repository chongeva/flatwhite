import logging
import collections

from six import string_types
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.auth import get_user_model

User = get_user_model()
logging.basicConfig()

logger = logging.getLogger('flatwhite')


def bulk_logentry_op(user_id, action_flag, obj, message=""):
    """Bulk create log entries. (AWESOME-ness!)

    Args:
        user_id: PK of user performing action.
        action_flag: ADDITION, CHANGE, DELETION.
        object_list: Objects to perform operation on.
        message: Operation message. ``Default=""``.

    .. note::
        In case of DELETION, this method must be called before the deletion.
    """
    if obj is not None:
        entries = []

        if isinstance(obj, collections.Iterable) and not isinstance(obj, string_types):
            object_list = obj
        else:
            object_list = [obj]

        for obj in object_list:
            if obj:
                try:
                    object_repr = str(obj)[:200]
                    try:
                        object_repr = str(obj.get_display_str())[:200]
                    except Exception as e:
                        pass
                except Exception as e:
                    logger.error('{0}'.format(e))
                    object_repr = int(obj.id)

                entries_kwargs = {
                    'user_id': int(user_id),
                    'content_type': ContentType.objects.get_for_model(obj, for_concrete_model=False),
                    'object_id': int(obj.id),
                    'object_repr': object_repr,
                    'action_flag': action_flag,
                    'change_message': message
                }
                entries.append(LogEntry(**entries_kwargs))

        logentries = LogEntry.objects.bulk_create(entries, batch_size=10000)
        return logentries


def log_addition(request, obj, message="", user_id=None):
    """
    Log that an object has been successfully added.
    The default implementation creates an admin LogEntry object.
    """
    try:
        if user_id is None:
            if hasattr(request, 'user') and request.user:
                user_id = request.user.id
        return bulk_logentry_op(user_id, ADDITION, obj, message)
    except Exception as e:
        logger.error('{0}'.format(e))


def log_addition_with_msg(request, obj, user_id=None):
    if request is None:
        user = User.objects.get(id=user_id)
    else:
        user = request.user
    user_display = user.get_full_name() or user.last_name or user.first_name or user.username
    msg = "Added by {0}".format(user_display)
    log_addition(request, obj, msg, user_id)


def log_deletion(request, obj, message="", user_id=None):
    """
    Log that an object has been successfully deleted.
    The default implementation creates an admin LogEntry object.

    .. note::
        This method must be called before the deletion.
    """
    try:
        if user_id is None:
            if hasattr(request, 'user') and request.user:
                user_id = request.user.id
        return bulk_logentry_op(user_id, DELETION, obj, message)
    except Exception as e:
        logger.error('{0}'.format(e))


def log_change(request, obj, message="", user_id=None):
    """
    Log that an object has been successfully changed.
    The default implementation creates an admin LogEntry object.
    """
    try:
        if user_id is None:
            if hasattr(request, 'user') and request.user:
                user_id = request.user.id
        return bulk_logentry_op(user_id, CHANGE, obj, message)
    except Exception as e:
        logger.error('{0}'.format(e))
