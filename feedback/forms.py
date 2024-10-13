from django import forms
from .models import OfferModel, ProblemModel, CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text']


class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferModel
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter offer title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter offer description'}),
        }


# Form for Problem
class ProblemForm(forms.ModelForm):
    class Meta:
        model = ProblemModel
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter problem title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter problem description'}),
        }

