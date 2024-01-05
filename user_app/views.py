from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'New User Account Created!, Login To get Started')
            return redirect('register')
    else:
        register_form = CustomUserCreationForm()

    context = {
        'register_form': register_form,
    }
    return render(request, 'register.html', context)