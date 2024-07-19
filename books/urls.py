
from django.urls import path
#from books.views import index, create
from books.views import BookDetailView, BookListView, BookCreateView, success

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('create/success/', success, name = 'success'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]