from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class AccountCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email','name','gender',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("you should Enter the same password above")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




class SupervisorCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email', 'name', 'gender')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("you should Enter the same password above")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.type=2
        user.is_staff=True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class AdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email', 'name', 'gender')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("you should Enter the same password above")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.type = 1
        user.is_staff = True
        user.is_superuser=True
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
