from django.shortcuts import render
from blog.serializers import UserSerializer, PostSerializer
from blog.models import Post
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from blog.permissions import IsOwnerOrReadOnIy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # reverse功能来返回完全限定的URL；
        'users2': reverse('users2-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
    })




class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnIy)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
