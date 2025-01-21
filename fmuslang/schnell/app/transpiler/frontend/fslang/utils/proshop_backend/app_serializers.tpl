from rest_framework import serializers
from .models import __TABLENAME_CASE__
# extra imports

class __TABLENAME_CASE__Serializer(serializers.ModelSerializer):

	class Meta:
		model = __TABLENAME_CASE__
		fields = '__all__'

	# extra members

