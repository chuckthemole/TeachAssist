from django import forms
from .models import *

CHOICES=[('public','public'), ('private','private')]

class Lesson_Form(forms.ModelForm):
    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = u'<p>Upload Image</p> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
    class Meta:
        model = Lesson
        fields = ["img"]

class Teacher_Form(forms.ModelForm):
    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = u'<p>Upload Image</p> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
    class Meta:
        model = teacher
        fields = ["img"]

class Public_Form(forms.Form):
    Public=forms.CharField(label='public', widget=forms.RadioSelect(choices=CHOICES))
