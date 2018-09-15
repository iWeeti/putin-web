from putin.models import Profiles
from .serializers import ProfileSerializer
from rest_framework.response import Response


# class ProfileViewSet(viewsets.ViewSet):

# 	def list(self, request):
# 		queryset = Profiles.objects.all()
# 		serializer = ProfileSerializer(queryset, many=True)
# 		return Response(serializer.data)


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profiles.objects.using('bot').all()
	serializer_class = ProfileSerializer