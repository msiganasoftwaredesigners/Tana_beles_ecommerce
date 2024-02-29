from django.urls import reverse_lazy
from django.views import generic
from django.db import IntegrityError
from allauth.socialaccount.providers.oauth2.views import OAuth2CallbackView
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"



class GoogleLoginCallbackView(OAuth2CallbackView):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except IntegrityError:
            # Handle the IntegrityError when email already exists
            # For example, you can redirect the user to the login page or display a message
            messages.error(request, 'You are already registered. Please log in.')
            return redirect('account_login')  # Use the appropriate login URL

