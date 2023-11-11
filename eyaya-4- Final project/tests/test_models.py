from django.test import TestCase
from store.models import *
from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Catergory.objects.create(name='django', slug='django')
        # test if the model is created successfully

    def test_category_model_entry(self):
        # check if the data has been inserted in database or not
        data = self.data1
        self.assertTrue(isinstance(data,Catergory))

    def test_category_model_entry(self):
        # check if the data returns name
        data = self.data1
        self.assertEqual(str(data),'django')

class TestBooksModel(TestCase):
    def setUp(self):
        Catergory.objects.create(name='django', slug='django')
        User.objects.create(username ='admin')
        self.data1 = Books.objects.create(catergory_id =1, title ='django beginners',author='django', created_by_id=1, 
                                          isbn= '978013475017',slug ="django-beginners", copies='20', image='django' )
        # test if the model is created 
        
    def test_Books_model_entry(self):
        # check if the data has been inserted in database or not
        data = self.data1
        self.assertTrue(isinstance(data,Books))
        
    def test_Books_model_entry(self):
        # check if the data returns name
        data = self.data1
        self.assertEqual(str(data),'django beginners')
