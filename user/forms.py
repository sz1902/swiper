from django import forms
from django.forms import ValidationError

from user.models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def clean_max_distance(self):
        cleaned_data = self.clean()
        min_distance = cleaned_data.get('min_distance')
        max_distance = cleaned_data.get('max_distance')
        if min_distance > max_distance:
            raise ValidationError('min distance > max distance')
        return max_distance


    def clean_max_dating_age(self):
        cleaned_data = self.clean()
        min_dating_age = cleaned_data.get('min_dating_age')
        max_dating_age = cleaned_data.get('max_dating_age')
        if min_dating_age > max_dating_age:
            raise ValidationError('min dating age > max dating age')
        return max_dating_age
