from django.shortcuts import render,redirect
from core.models import *
from datetime import date
from django.contrib import messages

# Create your views here.

def home(request):
    fooditem=food.objects.all()
    category_food=category.objects.all()
    data={'food':fooditem,
          'category':category_food }
    return render(request,'index.html',data)

def categories(request):
    categoryitem=category.objects.all()
    return render(request,'categories.html',{'data':categoryitem})

def category_foods(request,id):
   
    
    fooditem=food.objects.filter(cid=id)
    categoryitem=category.objects.get(id=id)
    

    '''data={'cat':categorys}'''
    return render(request,'category-foods.html',{'data':fooditem,'data1':categoryitem})

def foods_search(request):
    if request.method=='POST':
      data=request.POST.get('search')
      fooditem=food.objects.filter(ftitle__icontains=data)
      return render(request,'food-search.html',{'dt':fooditem,'search':data})


def foods(request):
    fooditem=food.objects.all()
    return render(request,'foods.html',{'data':fooditem})

def order(request,id):  
    fooditm=food.objects.get(id=id)
    return render(request,'order.html',{'data':fooditm})

def order1(request):
    if request.method=='POST':
        fooditm=request.POST.get('food')
        price=request.POST.get('price')
        qty=request.POST.get('qty')
        fname=request.POST.get('fullname')
        ph=request.POST.get('contact')
        em=request.POST.get('email')
        address=request.POST.get('address')
       
               
        today = date.today()
        qty1=int(qty)
        price1=int(price)
        tprice=qty1*price1
              
        
        
        oderitem=odeer(food=fooditm,
                       price=price,
                       qty=qty,
                       totalprice=tprice,
                       oder_date=today,
                       status='Odered',
                       customer_name=fname,
                       customer_contact=ph,
                       customer_email=em,
                       customer_address=address
                       )
        
        oderitem.save()
        messages.success(request, "Ordered successfully.")
       
        return redirect('/') 
    
        
        
        
    
