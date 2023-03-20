from django import forms

class MyForm(forms.Form):
    my_file = forms.FileField()
