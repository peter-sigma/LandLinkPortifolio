from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import BuyerSignUpForm, SellerSignUpForm, LawyerSignUpForm

def register(request):
    # Implement user registration logic here
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to a success page
            return redirect('registration_success')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def registration_success(request):
    return render(request, 'accounts/registration_success.html')

def buyer_signup(request):
    if request.method == 'POST':
        form = BuyerSignUpForm(request.POST)
        if form.is_valid():
            print("Valid form")
            user = form.save(commit=False)
            user.user_type = 'buyer'
            user.save()
            # Redirect to a success page
            return redirect('registration_success')
        else:
            print(user.user_type)
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        print("In get method")
        form = BuyerSignUpForm()
    return render(request, 'accounts/buyer_signup.html', {'form': form})

def seller_signup(request):
    if request.method == 'POST':
        form = SellerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'seller'
            user.save
            # Redirect to a success page
            return redirect('registration_success')
    else:
        form = SellerSignUpForm()
    return render(request, 'accounts/seller_signup.html', {'form': form})

def lawyer_signup(request):
    if request.method == 'POST':
        form = LawyerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_type = 'lawyer'
            user.save
            # Redirect to a success page
            return redirect('registration_success')
    else:
        print("In get instead of post")
        form = LawyerSignUpForm()
    return render(request, 'accounts/lawyer_signup.html', {'form': form})


def login_view(request):
    # Implement user login logic here
    return HttpResponse("in login view")

def logout_view(request):
    # Implement user logout logic here
    return HttpResponse("in logout view")

def password_reset_view(request):
    # Implement password reset logic here
    return HttpResponse("Reset password")

def password_reset_done(request):
    # Implement password reset done logic here
    return HttpResponse("password reset done")

def password_reset_confirm(request, uidb64, token):
    # Implement password reset confirmation logic here
    return HttpResponse("Password reset confirm")

def password_reset_complete(request):
    # Implement password reset complete logic here
    return HttpResponse("password reset complete")

