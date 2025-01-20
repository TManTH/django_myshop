from django.shortcuts import render
from django.http import HttpResponse
from appshop.models import Product, Country

def html_index(request):
    return render(request, 'appshop\index.html')
def index(request):
    count = Country.objects.get(id=1)
    Product.objects.create(
        name='tets',
        country=count,
        price=10000,
        description='test_phone'
    )
    #prod = Product.object.save()
    return (HttpResponse('DONE'))
