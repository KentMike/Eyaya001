from django.shortcuts import get_object_or_404 ,render

from .models import *

# list of categories
def categories(request):
    return {
        'categories':Catergory.objects.all()
            }

# Create your views here.
def all_books(request):
    my_books = Books.objects.all()
    return render(request,'store/home.html',{'my_books': my_books})

#create single page with book details
def book_details(request, slug):
    book = get_object_or_404 (Books, slug=slug , in_stock=True)
    return render(request,'store/products/detail.html', {'book': book})

# category_list():
def category_list(request, category_slug):
    category = get_object_or_404(Catergory, slug=category_slug)
    my_books = Books.objects.filter(catergory=category)
    return render(request, 'store/products/category.html', {'category': category, 'my_books': my_books})




    

