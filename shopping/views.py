from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from carton.cart import Cart
from catalog.models import Category, Product
from customs.models import Color, Quantity, Shipping, Finish

from .forms import CartItemForm

from .models import CartItem, Sale
from .forms import SalePaymentForm

def add(request, product_id):

    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        cart = Cart(request.session)
        form = CartItemForm(request.POST or None)
        if form.is_valid():
            item = form.save()
            item.final_cost = item.calculateFinalCost()
            c = item.final_cost
            print "Final "+str(item.final_cost)
            if item.rounded:
                if product.rounded_cost is None:
                    item.final_cost = c + product.category.rounded_cost
                else:
                    item.final_cost = c + product.rounded_cost
            cart.add(item, price=item.final_cost)
            return HttpResponseRedirect("/shopping/cart/")
        else:
            print form.errors
    else:
        form = CartItemForm(initial={'id':product_id})
    token = {}
    token['form'] = form
    token['quantities'] = product.quantities.all
    token['colors'] = product.colors.all
    token['finishes'] = product.finishes.all
    token['product'] = product
    if product.category.rounded and product.rounded:
        token['can_be_round'] = True
        token['rounded_cost'] = product.rounded_cost
        if product.rounded_cost is None:
            token['rounded_cost'] = product.category.rounded_cost
    else:
        token['can_be_round'] = False

    token.update(csrf(request))
    return render_to_response('tinbox/order.html', token)

def remove(request):
    cart = Cart(request.session)
    product = cart.products[int(request.GET.get('id'))]
    cart.remove(product)
    return HttpResponseRedirect("/shopping/cart/")

def show(request):
    return render(request, 'tinbox/show-cart.html')

def clear(request):
    cart = Cart(request.session)
    cart.clear()
    return HttpResponseRedirect('/shopping/cart')

def thanks(request):
    return render(request, 'tinbox/thank-you.html')

def charge(request):
    cart = Cart(request.session)
    if cart.unique_count > 0:
        if request.method == "POST":
            form = SalePaymentForm(request.POST or None)
            if form.is_valid(): # charges the card
                template = get_template('tinbox/order-response-email.html')
                context = Context({'cart': cart, 'total': cart.total, 'shipping_cost': form.cleaned_data.get("shipping"), 'name' : form.cleaned_data.get("name") })
                content = template.render(context)
                cart.clear()
                form_email = form.cleaned_data.get("email")
                form_name = form.cleaned_data.get("name")
                subject = 'Tinbox Solutions - Order Successfully Processed'
                from_email = settings.EMAIL_HOST_USER
                to_email = [form_email]
                msg = EmailMultiAlternatives(subject, "", from_email, to=to_email)
                msg.attach_alternative(content, "text/html")
                msg.send()
                return HttpResponseRedirect('/shopping/thank-you')
            else:
                t = form.determineShippingFormField(1, cart.total)
                return render_to_response("tinbox/charge.html", RequestContext( request, {'form': form, 'turnaround_cost' : t.turnaround_cost, 'turnaround' : t.turnaround} ) )
        else:
            form = SalePaymentForm()
            t = form.determineShippingFormField(1, cart.total)
        return render_to_response("tinbox/charge.html", RequestContext( request, {'form': form, 'turnaround_cost' : t.turnaround_cost, 'turnaround' : t.turnaround} ) )

    else:
        return render(request, 'tinbox/show-cart.html', {"empty": True})
