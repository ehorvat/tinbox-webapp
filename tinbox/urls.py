from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Registration URLs
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    # Auth-related URLs:
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/process_login/$', views.process_login, name='process_login'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/login_error/$', views.login_error, name='login_error'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/tinbox/accounts/login/'})

]
