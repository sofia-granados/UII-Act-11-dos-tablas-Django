from django.db import models

class Proveedor(models.Model):
    compañia = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    producto = models.CharField(max_length=100)
    precios = models.DecimalField(max_digits=10, decimal_places=2)
    entregas = models.IntegerField(default=0)
    licencia_permiso = models.CharField(max_length=50)
    
    def __str__(self):
        return self.compañia

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    cuidados = models.TextField()
    enfermedades = models.TextField(blank=True)
    especie = models.CharField(max_length=50)
    alimentacion = models.CharField(max_length=100)
    foto_animal = models.ImageField(upload_to='img_animales/', blank=True, null=True)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='animales')

    def __str__(self):
        return f"{self.nombre} - {self.especie}"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales"