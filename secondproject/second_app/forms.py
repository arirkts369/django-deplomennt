from django.forms import ModelForm
from second_app.models import Userdata

class myForm(ModelForm):
    class Meta:
        model = Userdata
        fields = ['fname','lname','email']
