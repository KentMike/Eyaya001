from django.urls import path
from .import views



app_name ='store'

urlpatterns = [
    path ('', views.all_books , name='all_books'),
    path ('item/<slug:slug>/', views.book_details , name='book'),
    path('categories/<slug:slug>/', views.category_list, name='category_list'),


]
