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


class BookAddForm(forms.ModelForm):
    model = Book
    fields = (
        'title', 'author', 'publish_year',
        'slug', 'featured_image', 'excerpt',
        'bookmarked', 'available', 'shelf'
    )
    widgets = {'publish_year': DateInput()}


class AuthorAddForm(forms.ModelForm):
    model = Author
    fields = ('author')
