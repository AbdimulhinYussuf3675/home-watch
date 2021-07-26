from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('signout')
    else:
        if request.user.id == 1:
            if request.method == 'POST':
                form = NeighborhoodForm(request.POST)
                if form.is_valid():
                    neighborhood = Neighborhood(neighborhood_name=request.POST['neighborhood_name'],neighborhood_location=request.POST['neighborhood_location'])
                    neighborhood.save()
                return redirect('index')
            else:
                form = NeighborhoodForm()
            neighborhoods = Neighborhood.objects.all()
            return render(request,'index.html',{'neighborhoods':neighborhoods,'form':form})
        elif request.user != 1:
            user = UserProfile.objects.filter(user = request.user).first()
            if user is None:
                user = UserProfile(user=request.user)
                user.save()
            if user.neighborhood is None:
                title = 'Neighborhood'
                neighborhoods = Neighborhood.objects.all()
                return render(request,'index.html',{'neighborhoods':neighborhoods})
            else:
                user = UserProfile.objects.filter(user = request.user).first()
                return redirect(reverse('neighborhood',args=[user.neighborhood.id]))

def signout(request):
    logout(request)
    return redirect('login')



