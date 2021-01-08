from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import models
from . import forms

class CreateMeal(CreateView):
    model = models.Meal
    form_class = forms.CreateMealForm
    #success_url = reverse_lazy('main')