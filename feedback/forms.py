from django import forms
from .models import OfferModel, ProblemModel, CommentModel


class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferModel
        fields = ['title', 'description', 'category']


class ProblemForm(forms.ModelForm):
    class Meta:
        model = ProblemModel
        fields = ['title', 'description']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text']
