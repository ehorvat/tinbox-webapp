from django.conf.urls import include, url
import views

app_name = 'product'

urlpatterns = [
    #url(r'^$', include('tinbox.urls', namespace="tinbox")),
    url(r'^(?P<product_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<product_id>[0-9]+)/subproducts/$', views.subproducts, name='subproducts'),
]
