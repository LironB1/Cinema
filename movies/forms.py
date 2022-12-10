from django.forms import ModelForm
from movies.models import Movie,Hall,Screening
from django.contrib.auth.models import User

 
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
 

class HallForm(ModelForm):
    class Meta:
        model = Hall 
        fields = '__all__'

class ScreeningForm(ModelForm): 
    class Meta:     
        model = Screening
        fields = "__all__"