from django import forms

class QueryForm(forms.Form):
    query = forms.CharField( required=True, label="Query (Single Query at a time)",widget= forms.TextInput
                           (attrs={'placeholder':'Enter your Query'}))
