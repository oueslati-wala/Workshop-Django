from django import forms
from .models import Conference

class ConferenceForm(forms.ModelForm):
    class Meta:
        model=Conference
        fields=['name','theme','location','descripption','start_date','end_date']
        labels={
            'name':"titre de la conference",
            'theme':"thmatique de la conference"
        }
        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':"entrez un titre a la conference"
                }
            ),
            'start_date':forms.DateInput(
                attrs={
                    'type':"date"
                }
            ),
            'end_date':forms.DateInput(
                attrs={
                    'type':"date"
                }
            )
        }   