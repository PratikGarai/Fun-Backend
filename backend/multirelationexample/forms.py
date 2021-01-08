from django import forms
from . import models

class CreateMealForm(forms.ModelForm):

    class Meta :
        model = models.Meal
        fields = '__all__'
    
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    
    members = forms.ModelMultipleChoiceField(
        queryset = models.Member.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )