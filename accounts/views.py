from django.shortcuts import render

# Create your views here.
from forms import RegistrationForm
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import TemplateView
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.contrib.auth.models import User
from catalog.models import Category


def register(request):
    page = 'registration/registration_form.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            page = 'registration/registration_complete.html'
            send_mail('Thank you for signing up with Tinbox', 'Thank you!', 'eric.horvat@gmail.com', [form.cleaned_data['email']], fail_silently=False)

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response(page, token)

# Create your views here.
def dashboard(request):
    context = {
        'username' : request.user.username,
        'products' : Category.objects.all(),
    }
    return render_to_response('tinbox/dashboard.html',context)
