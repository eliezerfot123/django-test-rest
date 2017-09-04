from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView, 
    )

from posts.models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug' #esto es para poder enfatizar que quiero que muestre los detalles por url
    #lookup_url_kwarg = "abc" #es para darle un nombre a la ur y asi el lookup le asignas un nombre



