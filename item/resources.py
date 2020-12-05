from import_export import resources
from item.models import PuestoTrabajo

class PuestoTrabajoResource(resources.ModelResource):
    class Meta:
        model: PuestoTrabajo

