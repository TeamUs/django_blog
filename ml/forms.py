# titanic_predictor/forms.py
from django import forms

class ModelChoiceForm(forms.Form):
    model_choices = [
        ('gradient_boosting', 'Градиентный бустинг'),
        ('polynomial_regression', 'Полиномиальная регрессия'),
        ('rnn', 'Рекуррентная нейронная сеть'),
    ]
    model = forms.ChoiceField(choices=model_choices)
