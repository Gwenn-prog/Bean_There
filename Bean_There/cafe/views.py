from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cafe
from .serializers import CafeSerializer
from .filters import CafeFilter
# Create your views here.


class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all() # Get all cafes
    serializer_class = CafeSerializer # To convert data to JSON


    # Enable search and filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # Built in functions for filtering, searching and ordering
    filterset_class = CafeFilter  #filter
    search_fields = ['name', 'about', 'menu', 'address']  # Allow text search
    ordering_fields = ['name']  # Enable ordering by name
     