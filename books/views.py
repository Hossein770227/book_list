from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy

from .models import Books

class BookListView(generic.ListView):
    model=Books
    paginate_by=4
    template_name='books/book_list.html'
    context_object_name='books'


class BookDetailView(generic.DetailView):
    model=Books
    template_name='books/book_detail.html'
    context_object_name='book'


class BookCreateView(generic.CreateView):
    model=Books
    fields=['title', 'author', 'description', 'price','cover']
    template_name='books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model=Books
    fields=['title', 'author', 'description', 'price','cover']
    template_name='books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model=Books
    template_name='books/book_delete.html'
    success_url=reverse_lazy('book_list')