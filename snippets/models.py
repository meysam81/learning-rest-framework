from django.db import models as db
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

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
    owner = db.ForeignKey('auth.User', related_name='snippets', on_delete=db.CASCADE)
    highlighted = db.TextField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
