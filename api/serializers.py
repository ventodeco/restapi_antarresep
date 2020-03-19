from rest_framework import serializers
from .models import Resep

class ResepSerializers(serializers.ModelSerializer):
	class Meta:
		model = Resep
		fields = '__all__'	