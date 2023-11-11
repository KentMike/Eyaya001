from django.http import JsonResponse  # Add this import

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from store.models import Books
from . basket import Basket

# Create your views here.
def basket_summary(request):
    basket= Basket(request)
    return render(request, 'store/basket/summary.html',{'basket':basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_qty = int(request.POST.get('bookqty'))
        book = get_object_or_404(Books, id=book_id)
       
        basket.add(book=book, book_qty=book_qty)  # Fixed variable name here (book_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'book_qty':basketqty})
        return response
