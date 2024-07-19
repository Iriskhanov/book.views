from django.shortcuts import render, redirect
# from django.views import View
from django.views.generic import ListView, CreateView, DetailView
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


def success(request):
    return render(request, 'success.html')




# def index(request):
#     book = Book.objects.all()
#     return render(request, 'index.html', {'books': book})

# def create(request):
#     if request.POST:
#         name = request.POST.get('name')
#         author = request.POST.get('author')
#         book = Book(name=name, author=author)
#         book.save()
#         return redirect('home')
#     return render(request, 'create.html')