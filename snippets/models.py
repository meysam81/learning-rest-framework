from django.db import models as db
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(db.Model):
    created = db.DateTimeField(auto_now_add=True)
    title = db.CharField(max_length=100, blank=True, default='')
    code = db.TextField()
    linenos = db.BooleanField(default=False)
    language = db.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = db.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.code
