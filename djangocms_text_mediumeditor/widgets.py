# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid

from django.forms.widgets import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class MediumEditorWidget(Textarea):
    template_name = 'cms/plugins/widgets/mediumeditor.html'
    def __init__(self, attrs=None):
        super(Textarea, self).__init__(attrs)
