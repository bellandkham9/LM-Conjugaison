from django import forms
from .models import *


class ConjugaisonForm(forms.ModelForm):
   
    class Meta:
        model=Etre_conjuguer
        fields=('Verbe','Langue','Temps_Verbaux',)


class RegisterConjugForm(forms.ModelForm):  
    class Meta:
        model=Etre_conjuguer
        fields = ('id','Verbe','Langue','Temps_Verbaux','person1','person2','person3','person4','person5','person6','audio') 