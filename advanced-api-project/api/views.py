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
