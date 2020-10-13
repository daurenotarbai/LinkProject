from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from .pagination import LinkPagePagination

class LinkListView(generics.ListAPIView):
    queryset = LinkModel.objects.all()
    serializer_class = LinkListSerializer
    pagination_class = LinkPagePagination

class CategoryListView(generics.ListAPIView):
    queryset = CategoryLink.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LinkPagePagination