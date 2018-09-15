from putin.models import Profiles
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profiles.objects.using('bot').all()
	serializer_class = ProfileSerializer