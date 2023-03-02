from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class PasswordChange(PasswordChangeForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('current_pass', 'new_pass', 'confirm_new_pass')