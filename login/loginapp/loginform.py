from django import forms
from loginapp.models import logindb

class logform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = logindb
        fields = '__all__'
        