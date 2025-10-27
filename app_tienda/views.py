from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .forms import AnimalForm

def listar_animales(request):
    animales = Animal.objects.all()
    return render(request, 'listar_animales.html', {'animales': animales})

def detalle_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'detalle_animal.html', {'animal': animal})

def crear_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_tienda:listar_animales')
    else:
        form = AnimalForm()
    return render(request, 'formulario_animal.html', {'form': form, 'titulo': 'Crear Animal'})

def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('app_tienda:detalle_animal', animal_id=animal.id)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'formulario_animal.html', {'form': form, 'titulo': 'Editar Animal'})

def borrar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        animal.delete()
        return redirect('app_tienda:listar_animales')
    return render(request, 'confirmar_borrar.html', {'animal': animal})