from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TasksSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'altcomp_app.tasks_system'
    verbose_name = _('Task system')
    verbose_name_plural = _('Task system')
