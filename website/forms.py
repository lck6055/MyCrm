from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignUp(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False) # Modifying the data before saving into database
        first = self.cleaned_data['first_name']
        last = self.cleaned_data['last_name']
        user.username = first + last # Use email as username
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit: # if commit --> true, stored to database else not
            user.save()
        return user