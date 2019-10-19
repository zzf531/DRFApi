from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from snippets2 import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets2', views.SnippetViewSet)
router.register(r'users2', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
