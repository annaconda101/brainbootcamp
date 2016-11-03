from __future__ import unicode_literals

from django.db import models

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LOG_TYPE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

class CbtLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    published = models.BooleanField(default=False)
    log_type = models.CharField(choices=LOG_TYPE_CHOICES, default='quick_add', max_length=100)

    class Meta:
        ordering = ('created',)
