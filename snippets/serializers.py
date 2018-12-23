from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'linenos', 'language', 'style')