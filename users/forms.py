from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from catalog.forms import FormStyleMixin

from users.models import User

class UserRegisterForm(FormStyleMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2') 


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')