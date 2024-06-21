from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            messages.success(request, f'Registration for {firstname} {lastname} was successful.')
            form.save()
            redirect('company_home')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request, 'customers/register.html', context=context)

@login_required
def my_accounts(request):
    return render(request, 'customers/my_account.html')