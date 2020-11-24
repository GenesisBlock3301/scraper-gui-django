from django import forms


class SearchForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'class': 'search', 'placeholder': 'Search URL'}),max_length=255)
