from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic.list import ListView
from .models import CustomUser
from .forms import BasicUserForm, PatientRegistrationForm, UserRegistrationForm

class UsersView(ListView):
    model = CustomUser
    template_name = 'users.html'
    context_object_name = 'users'

class RegisterUserView(View):
   def get(self, request):
     basic_form = BasicUserForm()
     context = {'basic_form': basic_form, 'form': None}
     return render(request, 'register_user.html', context)

   def post(self, request):
    form = None
    basic_form = BasicUserForm(request.POST)
    if basic_form.is_valid():
        role, email, phone, username = map(basic_form.cleaned_data.get, ['role', 'email', 'phone', 'username'])
        print(f"Role: {role}, Email: {email}, Phone: {phone}, Username: {username}")
        duplicate_check = {
            'username': CustomUser.objects.filter(username=username).exists(),
            'email': CustomUser.objects.filter(email=email).exists(),
            'phone': CustomUser.objects.filter(phone=phone).exists()
        }
        if any(duplicate_check.values()):
            duplicate_field = next(key for key, value in duplicate_check.items() if value)
            messages.error(request, f"A user with this {duplicate_field} already exists.")
        else:
            form = {'Patient': PatientRegistrationForm, 'Admin': UserRegistrationForm, 'Doctor': UserRegistrationForm}.get(role)
            if form:
                form = form(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    if role != 'Patient':
                        user.set_password(form.cleaned_data['password'])
                    user.save()
                    messages.success(request, "User saved successfully.")
                    return redirect('users')
                messages.error(request, "Form is not valid.")
                print(form.errors)
            else:
                messages.error(request, 'Invalid role specified.')
                return redirect('register_user')
    else:
        messages.error(request, "Basic form is not valid.")
        print(basic_form.errors)

    context = {'basic_form': basic_form, 'form': form}
    return render(request, 'register_user.html', context)
