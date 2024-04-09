from django import forms
from django.utils.translation import gettext_lazy as _

class ModelChoiceForm(forms.Form):
    model_choices = [
        ('gradient_boosting', _('Градиентный бустинг')),
        ('polynomial_regression', _('Полиномиальная регрессия')),
        ('rnn', _('Рекуррентная нейронная сеть')),
    ]
    model = forms.ChoiceField(choices=model_choices, label="")
