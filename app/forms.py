from django import forms
from .models import Efile

class NotesForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Notes type here...'}))
    class Meta:
        model = Efile
        fields = ['title']

class NotesUpdate(forms.ModelForm):
    class Meta:
        model = Efile
        fields = '__all__'
