from django.urls import path,include
from .views import *

urlpatterns = [
    
     path('',home,name='home'),
     path('categories/',categories,name='categories'),
     path('category_foods/<id>/',category_foods,name='category_foods'),
     path('food_search/',foods_search,name='foods_search'),
     path('foods/',foods,name='foods'),
     path('order/<int:id>/',order,name='order'),
     path('order1/',order1,name='order1')
     
     
    
    
]

