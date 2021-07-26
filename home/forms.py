from .models import Neighborhood,Business,UserProfile,Post
from django.contrib.auth.models import User
from django.forms import ModelForm

class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ('neighborhood_name',)

class UpdateProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','location')

class AddBusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ('name','email','business_location')

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_description',)
