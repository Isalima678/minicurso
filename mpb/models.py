
from django.db import models

class Musica(models.Model):
    titulo = models.CharField('Título', max_length=150)
    artista = models.CharField('Artista', max_length=150)
    album = models.CharField('Album', max_length=150)
    genero = models.CharField('Gênero', max_length=150)
    dt_lacamento = models.DateField('Lançamento', blank=True, null=True)
    audio = models.FileField('Arquivo')

    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musicas'

    def __str__(self):
        return self.titulo 

