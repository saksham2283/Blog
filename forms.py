from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
#from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password1):
            raise ValidationError("Password must contain at least one letter.")
        return password1


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'published_date': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',  # Format for datetime-local input
                attrs={'type': 'datetime-local'}  # HTML5 input type for datetime
            )
        }