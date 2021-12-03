from .models import Temp
from django.forms import ModelForm

class TempForm(ModelForm):
    class Meta:
        model = Temp
        fields = ['value']