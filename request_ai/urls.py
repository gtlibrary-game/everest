from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AIRequestViewSet

router = DefaultRouter()
router.register(r'request_ai', AIRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
