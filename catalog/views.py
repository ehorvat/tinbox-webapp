from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from django.http import JsonResponse
from .models import Category
# Create your views here.
def detail(request, product_id):
    category = get_object_or_404(Category, pk=product_id)
    category.category_name = category.category_name[:-1]
    return render(request, 'tinbox/detail.html', {'product': product})

@requires_csrf_token
def subproducts(request, product_id):
    category = get_object_or_404(Category, pk=product_id)
    return JsonResponse({'categories': product.categories })
