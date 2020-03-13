from django.contrib import admin
from .models import Operation, Piece, Station
# Register your models here.
admin.site.register(Operation)
admin.site.register(Piece)
admin.site.register(Station)