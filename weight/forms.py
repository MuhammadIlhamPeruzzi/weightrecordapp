from django import forms  
from weight.models import WeightRecord

class DateInput(forms.DateInput):
    input_type = 'date'
    
class WeightForm(forms.ModelForm):  
    class Meta:  
        model = WeightRecord  
        fields = "__all__"
        widgets = {
            'createdAt': DateInput()
        }