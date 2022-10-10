from .models import Issue, User_Detail
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ('return_by',)
        widgets = {'return_by': DateInput()}


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User_Detail
        fields = ('address', 'contact_no',)
