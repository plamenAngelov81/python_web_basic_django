from django import forms

from my_games_app.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'category', 'rating', 'max_level', 'image_url', 'summary']


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'category', 'rating', 'max_level', 'image_url', 'summary']


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Game
        fields = ['title', 'category', 'rating', 'max_level', 'image_url', 'summary']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []