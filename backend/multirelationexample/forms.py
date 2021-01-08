from django import forms
from . import models

class CreateMealForm(forms.ModelForm):

    class Meta :
        model = models.Meal
        fields = '__all__'
    
    date = forms.DateInput()
    members = forms.ModelMultipleChoiceField(
        queryset = models.Member.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )