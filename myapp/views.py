from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class AuthorList(generics.ListCreateAPIView):
    print("in the list serializer")
    queryset = Author.objects.all()
    print('queryset in the List',queryset)
    serializer_class = AuthorSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    print('queryset in the detail ',queryset)
    serializer_class = PostSerializer


class PostList(generics.ListCreateAPIView):
    print("in the list serializer")
    queryset = Post.objects.all()
    print('queryset in the List',queryset)
    serializer_class = PostSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    print('queryset in the detail ',queryset)
    serializer_class = AuthorSerializer