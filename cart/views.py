from django.shortcuts import render,redirect,get_object_or_404
from shop . models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_details(request,tot=0,count=0,cart_item=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_item=items.objects.filter(cart=ct,active=True)
        for i in ct_item:
            tot +=(i.prodt.price*i.quant)
            count+=i.quant
        
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_item,'t':tot,'cn':count})

def     c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.session.create()
    return ct_id

def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quant<c_items.prodt.stock:
            c_items.quant+= 1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quant=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')
# delete indivijual prodect

def del_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.quant>1:
        c_items.quant-= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect ('cartDetails')

# Remove entire product

def remv_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect ('cartDetails') 