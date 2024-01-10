from django import forms
from .models import ShortCourse



class ShortCourseForm(forms.ModelForm):
    class Meta:
        model = ShortCourse
        fields = ['title', 'subtitle', 'amount']


    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if isinstance(amount, int):
            return amount
        raise forms.ValidationError('Invalid amount. Please enter a valid number.')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) > 5 and title.isalpha():
            return title
        raise forms.ValidationError('Invalid title. Please enter a valid number.')

    def subtities(self):
        subtitle = self.cleaned_data.get('subtitle')
        if subtitle.isalpha() and len(subtitle) > 5:
            return subtitle
        raise forms.ValidationError('Invalid subtitle. Please enter a valid number.')   
    