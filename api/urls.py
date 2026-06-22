from .views import UserViewSet, liveness, readiness
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('health/live/', liveness, name='liveness'),
    path('health/ready/', readiness, name='readiness'),
] + router.urls
