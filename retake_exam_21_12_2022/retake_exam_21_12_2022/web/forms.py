from django import forms

from retake_exam_21_12_2022.web.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['plant_type', 'name', 'image_url', 'description', 'price']


class PlantEditForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['plant_type', 'name', 'image_url', 'description', 'price']


class PlantDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Plant
        fields = ['plant_type', 'name', 'image_url', 'description', 'price']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'profile_picture']


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
