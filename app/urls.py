from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewset, like, register, login

router = DefaultRouter()
router.register(r'posts', PostViewset, basename='posts')


urlpatterns = [
    path('api/like/<int:id>/', like, name='like'),
    path('api/register/', register, name='register'),
    path('api/login/', login, name='login'),
    path('api/', include(router.urls)),
]