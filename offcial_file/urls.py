from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls import include
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^', include('snippets.urls')),
    url('^blog/', include('blog.urls')),
    url('^api/', include('snippets2.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url('^schema/$', schema_view),

]
