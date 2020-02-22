from django.shortcuts import render, HttpResponse, redirect, render
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import LoginForm
from .models import Profile

# Create your views here.
def index(request):
    print(User)
    return render(request, 'index.html')


"""
    TODO: Class UserProfileView()

        Visualizar Perfil de Usuario
        Editar Perfil de Usuario

    path('login/', login, name='login'),
    path('new/', newUser, name='new'),
    path('logout/', logout, name='logout'),
    path('reset-password/', resetPassowrd, name='reset-password'),
    path('profile/', profile, name='profile'),

"""

class LoginView(LoginView):
    template_name = 'login.html'


class ProfileView(DetailView):
    context_object_name = 'profile'
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



def new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

