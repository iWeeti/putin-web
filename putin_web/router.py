from putin.api.viewsets import ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet)