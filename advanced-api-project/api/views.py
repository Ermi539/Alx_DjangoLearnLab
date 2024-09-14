from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
# api/views.py

class BookListView(generics.ListCreateAPIView):
    # ... (other code) 
    def create(self, request, *args, **kwargs):
        # You can add custom logic here before or after the standard creation process
        response = super().create(request, *args, **kwargs)
        # ... (additional logic if needed)
        return response
CreateView
UpdateView
DeleteView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import DjangoFilterBackend, SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']   class BookListView(generics.ListCreateAPIView):
       """
       Handles listing all books and creating new books.
       Allows filtering, searching, and ordering of books using query parameters.
       Requires authentication for creating, but allows unauthenticated users to view the list.
       """
       # ... (rest of the view code)
   
from django_filters import rest_framework
filters.OrderingFilter
filters.SearchFilter

