from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)

urlpatterns = ([
    path('', include(router.urls)),
    path('schema/', schema_view),
])
