from django import forms


class NumberForm(forms.Form):
    num1 = forms.IntegerField(label='Number1')
    num2 = forms.IntegerField(label='Number2')


class UserNameForm(forms.Form):
    username = forms.CharField(max_length=200, label='Enter Username')


class DataQueryForm(forms.Form):
    repo_count = forms.IntegerField(label='Enter Repo Count')
