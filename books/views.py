from django.shortcuts import render
from django.views import generic 

from .models import Books

class BookListView(generic.ListView):
    model=Books
    template_name='books/book_list.html'
    context_object_name='books'