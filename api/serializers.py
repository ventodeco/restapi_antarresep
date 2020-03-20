from rest_framework import serializers
from .models import Resep, Bahan, Kategori, Profil

class ResepSerializers(serializers.ModelSerializer):
	class Meta:
		model = Resep
		fields = '__all__'	

class BahanSerializers(serializers.ModelSerializer):
	class Meta:
		model = Bahan
		fields = '__all__'

class KategoriSerializers(serializers.ModelSerializer):
	class Meta:
		model = Kategori
		fields = '__all__'

class ProfilSerializers(serializers.ModelSerializer):
	class Meta:
		model = Profil
		fields = '__all__'
		
