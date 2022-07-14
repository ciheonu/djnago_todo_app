from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from accounts.forms import CustomUserCreationForm
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            subject = 'Welcome to Django ToDo App'
            message = f'Hi {first_name} {last_name}, /n Welcome to Django ToDo App'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            messages.success(request, f'Account created for { email } ! ')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


