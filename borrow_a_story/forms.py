from .models import Issue
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('issued_to', 'return_by',)
        widgets = {'return_by': DateInput()}
