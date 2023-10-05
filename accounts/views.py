from django.http import HttpResponse

from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required 
from .forms import UserRegistration
# Create your views here.
@login_required
def profile(request: HttpRequest) -> HttpResponse:
    template_name = 'accounts/profile.html'
    context = {
        'session': 'profile'
    }
    return render(request, template_name, context)




def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {})
        else:
            # Gérer le cas où le formulaire n'est pas valide
            return HttpResponse("Le formulaire n'est pas valide")
    else:
        user_form = UserRegistration()
        return render(request, 'accounts/register.html', {'user_form': user_form})