from store.models import Books

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey', {})
        self.basket = basket

    def add(self, book, book_qty=1):
        book_id = str(book.id)
        if book_id not in self.basket:
            self.basket[book_id] = {'copies': book.copies, 'quantity':int(book_qty) }
        else:
            self.basket[book_id]['quantity'] += book_qty

        self.save()

    def save(self):
        self.session['skey'] = self.basket
        self.session.modified = True
    
    def __iter__(self):
        books_ids = self.basket.keys()
        books = Books.objects.filter(id__in = books_ids)
        basket = self.basket.copy()

        for book in books:
            basket[str(book.id)]['book'] = book

        for item in basket.values():
            item['total_qty'] = item['copies'] * 1 
            yield {'book': book,
                'quantity': self.basket[str(book.id)]['quantity'],}
             # This doubles the 'copies' value



    
    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())
    
    def total_qty(self):
        return sum(item['copies'])

