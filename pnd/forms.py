from django import forms

class SearchForm(forms.Form):
    szukaj = forms.CharField(max_length=100)