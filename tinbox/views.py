from forms import RegistrationForm
from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import TemplateView
from django.core.context_processors import csrf
from django.core.mail import send_mail


class IndexView(TemplateView):
    template_name = "tinbox/index.html"

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail('Thank you for signing up with Tinbox!', 'Cool message that makes me feel acknowledged!', 'eric.horvat@gmail.com', [form.cleaned_data['email']], fail_silently=False)
            return HttpResponseRedirect('/tinbox/accounts/register/complete')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/register.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')

def login(request):
    token = {}
    token.update(csrf(request))
    return render_to_response('registration/login.html', token)

def process_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/tinbox/accounts/loggedin')
    else:
        return HttpResponseRedirect('/tinbox/accounts/login_error')

def loggedin(request):
    return render_to_response('registration/loggedin.html',
                              {'username': request.user.username})

def login_error(request):
    return render_to_response('registration/login_error.html')
