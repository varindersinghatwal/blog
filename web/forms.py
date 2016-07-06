from django import forms
from django.utils.translation import ugettext_lazy as _

class ArticleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=_("Title"), required=True)
    plain_txt = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label=_("Description"), required=True)

class CreateCommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'required':False, 'class': 'form-control', 'rows':4}), label=_("Comment"))
