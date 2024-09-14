from django.shortcuts import get_object_or_404, redirect, render
from .models import Game

# Create your views here.
def home(request):
    games_list = Game.objects.all()
    return render(request, 'home/index.html', {'games': games_list})

def controlGame(request):
    games_list = Game.objects.all()
    return render(request, 'controlGame/control.html', {'games': games_list})

def registerGame(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        precio = request.POST['numPrecio']
        plataforma = request.POST['txtPlataforma']
        imagenes = request.FILES.get('imgImagen')
        
        game = Game.objects.create(codigo=codigo, nombre=nombre, descripcion=descripcion, precio=precio, plataforma=plataforma, imagenes=imagenes)
        return redirect('control')
    else:
        return redirect('control')

def editGame(request, codigo):
    game = get_object_or_404(Game, codigo=codigo)
    return render(request, 'controlGame/editGame.html', {'game': game})

def gameEdition(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        precio = request.POST['numPrecio']
        plataforma = request.POST['txtPlataforma']
        imagenes = request.FILES.get('imgImagen', None)
        
        if ',' in precio:
            precio = precio.replace(',', '.')
            
        game = get_object_or_404(Game, codigo=codigo)
        game.nombre = nombre
        game.descripcion = descripcion
        game.precio = precio
        game.plataforma = plataforma
        if imagenes:
            game.imagenes = imagenes
        game.save()
        
        return redirect('control')
    else:
        return redirect('control')


def deleteGame(request, codigo):
    game = get_object_or_404(Game, codigo=codigo)
    game.delete()
    return redirect('control')