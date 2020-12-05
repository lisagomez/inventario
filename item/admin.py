from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PerfilDePuesto, Personal, NivelDeConfidencialidad, ComponenteNegocio, Componente, Dispositivo, Item, PuestoTrabajo
from .forms import ComputerForm, PersonalForm, PerfilDePuestoForm

@admin.register(PuestoTrabajo)
class PuestoTrabajoAdmin(ImportExportModelAdmin):
    list_display = ("comp_neg", "responsable", "puesto_trabajo","ip_add","fecha_fabricacion")
    pass

class ComputerAdmin(admin.ModelAdmin):
    list_display = ["comp_neg", "responsable", "puesto_trabajo","ip_add","fecha_fabricacion"]
    form = ComputerForm
    list_filter = ['comp_neg', 'ip_add', 'puesto_trabajo']
    search_fields = ['ip_add', 'comp_neg','puesto_trabajo']

class PerfilDePuestoAdmin(admin.ModelAdmin):
    list_display = ["descripcion_perfil_puesto","activo"]
    form = PerfilDePuestoForm
    
class PersonalAdmin(admin.ModelAdmin):
    list_display = ["componente_negocio","perfil_puesto","nombre", "apellido_paterno", "apellido_materno","nivel_confidencialidad"]
    form = PersonalForm
    list_filter = ["componente_negocio"]
    search_fields = ["componente_negocio","nombre", "apellido_paterno"]

admin.site.register(Dispositivo)
admin.site.register(Componente)
admin.site.register(Item)
admin.site.register(ComponenteNegocio)
admin.site.register(PerfilDePuesto)
admin.site.register(NivelDeConfidencialidad)
admin.site.register(Personal, PersonalAdmin)

