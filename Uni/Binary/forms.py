from django import forms


class NumberForm(forms.Form):
    num1 = forms.IntegerField(label='Number1')
    num2 = forms.IntegerField(label='Number2')
