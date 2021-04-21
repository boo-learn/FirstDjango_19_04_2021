from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.main),
    path('items/', views.items_list),
    path('item/<int:id>/', views.item),
]
