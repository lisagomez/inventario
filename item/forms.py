from django import forms
from .models import PuestoTrabajo, Personal, PerfilDePuesto

class ComputerForm(forms.ModelForm):
    class Meta:
        model = PuestoTrabajo
        fields = ["comp_neg", "responsable", "puesto_trabajo","ip_add","fecha_fabricacion",]

class PerfilDePuestoForm(forms.ModelForm):
    class Meta:
        model = PerfilDePuesto
        fields = ["codigo_perfil_puesto", "descripcion_perfil_puesto","activo"]

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ["componente_negocio","perfil_puesto", "nombre", "apellido_paterno", "apellido_materno","nivel_confidencialidad","activo"]