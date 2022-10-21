from django.contrib import admin
from .models import Musica


class MusicaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'artista', 'genero', 'dt_lacamento']
    

admin.site.register(Musica, MusicaAdmin)