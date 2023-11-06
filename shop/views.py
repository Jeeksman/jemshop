
from django.shortcuts import get_object_or_404, render
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prod_list=None
    cat=categ.objects.all()

    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prod_list=products.objects.filter(category=c_page,available=True)
    else:
        prod_list=products.objects.all().filter(available=True)
    paginator=Paginator(prod_list,4)
    try:
        page=int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        prod=paginator.page(page)
    except (EmptyPage,InvalidPage):
            prod=paginator.page(paginator.num_pages)
    return render(request,'home.html',{'prod':prod,'ct':cat})
    

def proDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'prod':prod})

def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'prod':prod})