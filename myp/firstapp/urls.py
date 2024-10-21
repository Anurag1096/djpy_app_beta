from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet,home,about

router = DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("home/",home,name='home'),
    path("about/",about,name="about"),
]