from django.db import models

# sucursales
class Ofc(models.Model):
    ubicacion = models.TextChoices('Corporativo', 'Sucursal')
    desc = models.TextField()
    tipo = models.CharField

    def __str__(self):
        return self.name + self.desc

class Dep(models.Model):
    loc = models.ForeignKey("Ofc.Model", verbose_name="Ubicación", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Departamento",max_length=3)
    desc = models.TextField()

    def __str__(self):
        return self.name + self.desc

class Ceco(models.Model):
    name = models.CharField(verbose_name="Centro de Costo",max_length=3)
    
    def __str__(self):
        return self.name 
