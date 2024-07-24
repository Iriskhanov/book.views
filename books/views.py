from django.urls import reverse_lazy
from django.shortcuts import render, redirect
# from django.views import View
from django.views.generic import DeleteView, ListView, CreateView, DetailView, UpdateView
from books.models import Book

class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author', 'description', 'image']
    template_name = 'create.html'
    success_url = 'success'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'author', 'image', 'description']
    template_name = 'book_update.html'
    success_url = '/create/success'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('home')

def success(request):
    return render(request, 'success.html')

