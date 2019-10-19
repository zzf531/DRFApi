from rest_framework import serializers
from blog.models import Post

from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username'),

    class Meta:
        model = Post
        fields = ('title', 'body', 'created_time', 'modified_time', 'excerpt', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippetss = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippetss')


