from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
generics.ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
       from rest_framework.authtoken.views import obtain_auth_token
   from rest_framework.authtoken.models import Token 
   from rest_framework.permissions import IsAuthenticated

   # ... other imports

   class BookViewSet(viewsets.ModelViewSet):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [IsAuthenticated] 

   # ... other views

   urlpatterns = [
       # ... other patterns
       path('api-token-auth/', obtain_auth_token), 
   ]
      class BookViewSet(viewsets.ModelViewSet):
       queryset = Book.objects.all()
       serializer_class = BookSerializer
       permission_classes = [IsAuthenticated]
rest_framework.permissions.IsAuthenticated
   



