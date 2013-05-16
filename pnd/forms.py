from django import forms

class SearchForm(forms.Form):
    szukaj = forms.CharField(max_length=100)

class NewsletterForm(forms.Form):
	imie = forms.CharField(max_length=150)
	email = forms.CharField(max_length=150)