from django import forms
from .models import Parcel,Client

class RegisterParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['adress_dep','adress_arr','weight']
        
class RegisterClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom','prenom','date_n']