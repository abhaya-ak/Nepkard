from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter email"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password"
        })
    )
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"})
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password1") != cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-select"}),
            "locality": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "pin": forms.NumberInput(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-select"}),
            "mobile": forms.TextInput(attrs={"class": "form-control"}),
            "job_city": forms.TextInput(attrs={"class": "form-control"}),
            "profile_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "my_file": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }