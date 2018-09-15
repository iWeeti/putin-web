from rest_framework import serializers
from putin.models import Profiles


class ProfileSerializer(serializers.HypelinkedModelSerializer):

	class Meta:
		model = Profiles
		fields = ('description', 'bday', 'cash', 'experience')
			