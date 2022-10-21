from wsgiref.util import request_uri
from django.shortcuts import render, redirect, get_object_or_404
from .models import Musica

from .forms import MusicaForm

def hello(request):
   return render (request, 'base.html')
   
def musicas(request):
   dados = Musica.objects.all()
   return render(request, 'album.html', {'musicas': dados})

def deletar(request, pk):
   dado = Musica.objects.get(pk=pk)
   dado.delete()
   return redirect('musicas')

def adicionar(request):
   if request.method == 'POST':
      form = MusicaForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return redirect('musicas')
   else:
      form = MusicaForm
      return render(request, 'nova_musica.html', {'form': form})      


def editar(request, pk):
   musica = get_object_or_404(Musica, pk=pk)
   form = MusicaForm(instance=musica)

   if (request.method == 'POST'):
      form = MusicaForm(request.POST, instance=musica)

      if (form.is_valid()):
         musica.save()
         return redirect('musicas')
      else:
         return render(request, 'editar.html', {'form': form, 'musica': musica})
   else:
      return render(request, 'editar.html', {'form': form, 'musica': musica})




def visualizar(request):
    musica = Musica.objects.all()    
    return render(request, 'ver.html', {'dados': musica})
