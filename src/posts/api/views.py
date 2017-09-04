from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.models import Post
from .serializers import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug' #esto es para poder enfatizar que quiero que muestre los detalles por url
    #lookup_url_kwarg = "abc" #es para darle un nombre a la ur y asi el lookup le asignas un nombre
    


