from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import * 
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets

""" Первый способ """

@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)
    else:
        return Response({'message': 'Hello Makers!!!'})
    
""" Второй способ """

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        post = request.data
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response(serializer.data)

""" Третий способ """

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostImageView(generics.ListAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer


""" Четвёртый способ """

class PostViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = PostSerializer

    def get_serializer_context(self):
        return {'request': self.request} 