from django.conf.urls import url, patterns


urlpatterns = patterns('shopping.views',
    url(r'^(?P<product_id>[0-9]+)/add', 'add', name='shopping-cart-add'),
    url(r'^remove/$', 'remove', name='shopping-cart-remove'),
    url(r'^cart/$', 'show', name='shopping-cart-show'),
    url(r'^clear/$', 'clear', name='shopping-cart-clear'),
    url(r'^checkout/$', 'charge', name="shopping-cart-charge"),
    url(r'^thank-you/$', 'thanks', name="shopping-cart-thanks"),
)
