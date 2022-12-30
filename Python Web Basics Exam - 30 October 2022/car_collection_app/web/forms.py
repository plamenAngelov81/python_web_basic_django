from django import forms

from car_collection_app.web.models import Profile, Car


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']


class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']


class CarDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []
