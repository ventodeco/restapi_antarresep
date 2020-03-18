from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profil)
admin.site.register(Kategori)
admin.site.register(Bahan)
admin.site.register(Resep)
admin.site.register(Order)