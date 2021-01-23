from django import forms
from .models import *

class Sport_Location_Form(forms.ModelForm):
    def as_p(self):
        "Returns this form rendered as HTML <p>s."
        return self._html_output(
            normal_row = u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
            error_row = u'%s',
            row_ender = '</p>',
            help_text_html = u' <span class="helptext">%s</span>',
            errors_on_separate_row = True)
    class Meta:
        model = Location
        fields = ["sport_location_img"]
        #exclude = ('teacher', 'location')

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
