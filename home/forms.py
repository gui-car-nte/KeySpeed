from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile, Keyboard


class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ['type', 'brand', 'model']

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=30)
    keyboard_type = forms.ChoiceField(choices=Keyboard.TYPE_CHOICES)
    keyboard_brand = forms.CharField(max_length=30)
    keyboard_model = forms.CharField(max_length=40)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'nickname', 'keyboard_type', 'keyboard_brand', 'keyboard_model')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nickname = self.cleaned_data['nickname']
        if commit:
            user.save()
            keyboard = Keyboard.objects.create(
                type=self.cleaned_data['keyboard_type'],
                brand=self.cleaned_data['keyboard_brand'],
                model=self.cleaned_data['keyboard_model'],
            )
            user.favourite_keyboards = keyboard
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(max_length=30)
    keyboard_type = forms.ChoiceField(choices=Keyboard.TYPE_CHOICES)
    keyboard_brand = forms.CharField(max_length=30)
    keyboard_model = forms.CharField(max_length=40)

    class Meta:
        model = UserProfile
        fields = ('username', 'nickname', 'keyboard_type', 'keyboard_brand', 'keyboard_model')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nickname = self.cleaned_data['nickname']
        if commit:
            user.save()
            if user.favourite_keyboards:
                user.favourite_keyboards.type = self.cleaned_data['keyboard_type']
                user.favourite_keyboards.brand = self.cleaned_data['keyboard_brand']
                user.favourite_keyboards.model = self.cleaned_data['keyboard_model']
                user.favourite_keyboards.save()
            else:
                keyboard = Keyboard.objects.create(
                    type=self.cleaned_data['keyboard_type'],
                    brand=self.cleaned_data['keyboard_brand'],
                    model=self.cleaned_data['keyboard_model'],
                )
                user.favourite_keyboards = keyboard
                user.save()
        return user