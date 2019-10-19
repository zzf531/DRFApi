from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns =[
    url(r'^$', views.api_root),
    url(r'^posts/$', views.PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post-detail'),

    url(r'^users2/$', views.UserList.as_view(), name='users2-list'),
    url(r'^users2/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name= 'users2-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

