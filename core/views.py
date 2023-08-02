from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def categories(request):
    return render(request,'categories.html')

def category_foods(request):
    return render(request,'category-foods.html')

def foods_search(request):
    return render(request,'foods-search.html')


def foods(request):
    return render(request,'foods.html')

def order(request):
    return render(request,'order.html')


    
