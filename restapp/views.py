from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()#queries postable and returns all objects
    serializer_class = PostSerializer#serializing queryset so it would be in a json format

