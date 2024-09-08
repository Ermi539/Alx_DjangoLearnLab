   from django.urls import path
   from . import views

   urlpatterns = [
       path('books/', views.BookListView.as_view()),
       path('books/<int:pk>/', views.BookDetailView.as_view()),
]
books/create
books/update
books/delete
   
