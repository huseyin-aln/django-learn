from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = '__all__'  # fetch all fields
        exclude = ('user',) # Bring all fields except user  # We put "," at the end because we are using a single element tupple


#? 2. method extend
# from .models import User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class UserForm(UserCreationForm):

#     class Meta():
#         model = User
#         # fields = '__all__'
#         fields = ('email', 'password1', 'password2')
#         # exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', )

