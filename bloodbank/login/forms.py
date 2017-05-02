from django import forms
from .models import Record


class DonateForm(forms.ModelForm):
    choice1 = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    blood_group = forms.ChoiceField(choices=choice1, initial='O Positive')

    class Meta:
        model = Record
        fields = ('donar_name', 'id_no', 'blood_group', 'units', 'date')
