# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from . import settings
from .sanitizer import clean_html


__all__ = ("MediumEditorText",)


class MediumEditorText(CMSPlugin):
    body = models.TextField(verbose_name=_("body"))
    class Meta:
        verbose_name = _("text")
        verbose_name_plural = _("texts")

    def __str__(self):
        return Truncator(strip_tags(self.body)).words(3, truncate="...")

    def save(self, **kwargs):
        # Override `save` method so that HTML can be sanitized.
        if settings.TEXT_MEDIUMEDITOR_HTML_SANITIZE:
            self.body = clean_html(self.body)
        super(MediumEditorText, self).save(**kwargs)
