from django import forms

class DuckEntry(forms.Form):
    content = forms.Textarea()
