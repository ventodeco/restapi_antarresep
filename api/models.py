from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
	JENIS_KELAMIN = (
		('Laki-laki', 'Laki-laki'),
		('Perempuan', 'Perempuan'),
	)
	KABKOT = (
    	('Kabupaten', 'Kabupaten'),
      	('Kota', 'Kota'),
    )
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	gambar = models.ImageField(null=True)
	firstname = models.CharField(max_length=255, null=False)	
	lastname = models.CharField(max_length=255, null=True)
	jenisKelamin = models.CharField(max_length=255, null=False, choices=JENIS_KELAMIN)
	nomorHp = models.CharField(max_length=255, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	jalan = models.CharField(max_length=500, null=True)
	kecamatan = models.CharField(max_length=255, null=True)
	kabkot = models.CharField(max_length=255, null=True, choices=KABKOT)
	kota = models.CharField(max_length=255, null=True)
	prov = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.firstname 

class Kategori(models.Model):
	name = models.CharField(max_length=255, null=False)
	
	def __str__(self):
		return self.name
 
class Bahan(models.Model):
	nama = models.CharField(max_length=255, null=False)
	harga = models.FloatField(max_length=255, null=False)
	kuantitas = models.FloatField(max_length=255, null=False)

	def __str__(self):
		return self.nama

class Resep(models.Model):
	nama = models.CharField(max_length=255, null=False)
	gambar = models.ImageField(null=True)
	harga = models.FloatField(max_length=255, null=False)
	deskripsi = models.TextField(max_length=255, null=False)
	kategori = models.ManyToManyField(Kategori)
	bahan = models.ManyToManyField(Bahan)

	def __str__(self):
		return self.nama
 
class Order(models.Model):
	STATUS = (
		('Pending', 'Pending'),
		('Sedang diproses', 'Sedang diproses'),
		('Sedang dikirim', 'Sedang dikirim'),
		('Telah diterima', 'Telah diterima'),
	)
	user = models.ForeignKey(Profil,null=True, on_delete=models.SET_NULL)
	resep = models.ForeignKey(Resep,null=True, on_delete=models.SET_NULL)
	status = models.CharField(max_length=255, null=True, choices=STATUS)
	note = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.resep.name


# class Rating(models.Model):
	