from django import forms
from . import models

class CreateMealForm(forms.ModelForm):

    class Meta :
        model = models.Meal
        fields = '__all__'