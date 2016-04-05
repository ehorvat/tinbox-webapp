from django.shortcuts import render
from django.views.generic import TemplateView
from catalog.models import Category
# Create your views here.
def index(request):
    return render(request, 'tinbox/index.html', {'categories': Category.objects.all()})
