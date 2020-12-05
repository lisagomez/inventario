from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

Activo = True
Inactivo = False
 
#catalogo componente: tarjeta madre...
class Componente(models.Model):
    tipo_componente = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo_componente

    class Meta:
        verbose_name_plural = 'Componentes'

#catalogo dispositivo: cpu, periféricos...
class Dispositivo(models.Model):
    TIPO_DISPOSITIVO_CHOICES = [
        ('PR', 'Periferico'),
        ('PC', 'CPU'),
        ('LT', 'LapTop'),
    ]
    NOMBRE_DISPOSITIVO_CHOICES = [
        ('TD', 'Teclado'),
        ('MS', 'Mouse'),
        ('MT', 'Monitor'),
        ('LC', 'Lectora'),
        ('PR', 'Impresora'),
        ('MP', 'Miniprinter'),
        ('PC', 'CPU'),
        ('LT', 'LapTop'),
    ]
    tipo_dispositivo = models.CharField(max_length=40, choices=TIPO_DISPOSITIVO_CHOICES,default='CPU')
    nombre_dispositivo = models.CharField(max_length=50, choices=NOMBRE_DISPOSITIVO_CHOICES,default='CPU')
        
    def __str__(self):
        return self.tipo_dispositivo + self.nombre_dispositivo

    class Meta:
        verbose_name_plural = 'Dispositivos'

#Alta de los componentes del equipo
class Item(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete = models.CASCADE)
    componente = models.ForeignKey(Componente, null=True, on_delete=models.SET_NULL)
    nombre_id = models.CharField(max_length=30)
    fabricante = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    capacidad = models.CharField(max_length=45)
    serie = models.CharField(max_length=45)
    entradas = models.CharField(max_length=45)
    slug = models.SlugField()
    desc = models.TextField(default="Sin observaciones")
    
    def __str__(self):
        return self.componente.tipo_componente + self.nombre_id

    class Meta:
        verbose_name_plural = 'Items-Componentes'

# Componentes de negocio de Mexicana de Abarrotes
class ComponenteNegocio(models.Model):
    # Constantes
    UNO = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5

    # Tipos de componentes de negocios
    TipoComponenteNegocios_Choices = [
        (UNO, 'CORPORATIVO'),
        (DOS, 'DIVISIÓN'),
        (TRES, 'ÁREA'),
        (CUATRO, 'DEPARTAMENTO o SUCURSAL'),
    ]
    descripcion_componente_negocio = models.CharField(max_length=150, help_text="Descripción del Componente de Negocios", verbose_name="Descripción del componente de negocios", blank=False, null=False, default=None)
    descripcion_corta_componente_negocio = models.CharField(max_length=50, help_text="Descripción Corta del Componente de Negocios", verbose_name="Descripción Corta del componente de negocios", blank=False, null=False, default=None)
    tipo_componente_negocio = models.SmallIntegerField(choices = TipoComponenteNegocios_Choices, default=UNO, help_text="(1) Corporativo o (2) División (MexAba/Hotelería)", verbose_name="Tipo de Componente de Negocios")
    codigo_componente_negocio = models.CharField(max_length=2, help_text="Código para identificar el Componente de Negocios", verbose_name="Código para identificar la Clasificación de la Organización", blank=False, null=False, default=None)
    slug = models.SlugField()
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Depende de')
    activo = models.BooleanField(blank=False, null=False, default=True, editable=True, help_text='Estado Lógico del Registro (Activo|Inactivo)', verbose_name='Activo')

    def _TipoComNegTXT(self):
        var1 = self.get_tipo_componente_negocio_display()
        return var1
    tipo_componente_negocio_TXT = property(_TipoComNegTXT)

    def __str__(self):
        return u'%s-%s' % (self.codigo_componente_negocio, self.descripcion_corta_componente_negocio, )

    class Meta:
        ordering = ('codigo_componente_negocio','descripcion_corta_componente_negocio',)
        verbose_name_plural = "Componentes de Negocio"

# Catálogo Niveles de Confidencialidad 
class NivelDeConfidencialidad(models.Model):
    descripcion_nivel_confidencialidad = models.CharField(max_length=50, help_text="Descripción del Nivel de Confidencialidad", verbose_name="Descripción del Nivel de Confidencialidad", blank=False, null=False, default=None)
    nivel_confidencialidad = models.IntegerField(default=0, validators=[MaxValueValidator(100),MinValueValidator(0)], help_text="100 - Mayor de Nivel de Acceso, 0 - Nulo nivel de acceso", verbose_name="Nivel de Confidencialidad")
    activo = models.BooleanField(default=Activo, help_text='Estado Lógico del Registro (Activo/Inactivo)', verbose_name='Activo', blank=False, null=False)

    def __str__(self):
        return u'%s (%s)' % (self.descripcion_nivel_confidencialidad, self.nivel_confidencialidad)
    
    class Meta:
        ordering = ('nivel_confidencialidad','descripcion_nivel_confidencialidad',)
        verbose_name_plural = "Niveles de Confidencialidad"

# relacionados con las organizaciones, relacionado con los niveles de confidencialidad, área y departamentos
class PerfilDePuesto(models.Model):
    descripcion_perfil_puesto = models.CharField(max_length=150, help_text="Descripción del Perfil de Puesto", verbose_name="Descripción del Nivel de Confidencialidad", blank=False, null=False, default='DIRECTOR')
    nivel_confidencialidad_default = models.ForeignKey(NivelDeConfidencialidad, on_delete=models.CASCADE)
    codigo_perfil_puesto = models.CharField(max_length=2, help_text="Código para identificar el Perfil de Puesto", verbose_name="Código para identificar el Perfil del Puesto", blank=False, null=False, default=None)
    activo = models.BooleanField(blank=False, null=False, default=True, editable=True, help_text='Estado Lógico del Registro (Activo|Inactivo)', verbose_name='Activo')

    class Meta:
        ordering = ('codigo_perfil_puesto', 'descripcion_perfil_puesto', )
        verbose_name_plural = 'Perfiles de Puestos'
    
    def __str__(self):
        return u'%s-%s (%s)' % (self.codigo_perfil_puesto, self.descripcion_perfil_puesto, self.nivel_confidencialidad_default)

# Recursos humanos alta de personal de Mexicana de Abarrotes
class Personal(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del Personal", verbose_name="Nombre de la persona", blank=False, null=False, default=None)
    apellido_paterno = models.CharField(max_length=100, help_text="Apellido Paterno", verbose_name="Apellido Paterno", blank=False, null=False, default=None)
    apellido_materno = models.CharField(max_length=100, help_text="Apellido Materno", verbose_name="Apellido Materno", blank=False, null=False, default='X')
    componente_negocio = models.ForeignKey(ComponenteNegocio, on_delete=models.CASCADE, help_text='Componente (Depto., Área, Sucursal) de Negocio al que está asignado', verbose_name = 'Asignado a')
    perfil_puesto = models.ForeignKey(PerfilDePuesto, on_delete=models.CASCADE, help_text='Perfil de puesto del personal', verbose_name='Perfil de Puesto')
    activo = models.BooleanField(blank=False, null=False, default=True, editable=True, help_text='Estado Lógico del Registro (Activo|Inactivo)', verbose_name='Activo')
    nivel_confidencialidad = models.ForeignKey(NivelDeConfidencialidad, on_delete=models.CASCADE, help_text='Nivel de Confidencialidad Asignado al Personal', verbose_name='Nivel de Confidencialidad')
    
    @property
    def nombre_completo(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    def __str__(self):
        return u'%s - %s %s %s (%s)' % (self.componente_negocio.codigo_componente_negocio, self.nombre, self. apellido_paterno, self.apellido_materno, self.nivel_confidencialidad.activo)
    
    class Meta:
        ordering = ('componente_negocio','perfil_puesto','nivel_confidencialidad','nombre','apellido_paterno', 'apellido_materno',)
        verbose_name_plural = 'Personal'

#Identifica la ubicación del equipo: PC01Auditoria, ACASUP01..., 
#Relaciona el equipo y sus componentes.
class PuestoTrabajo(models.Model):    
    TIPO_ACTIVO_CHOICES = [
        ('BJ', 'Baja'),
        ('PB', 'Programar Baja'),
        ('AC', 'Activo'),
    ]
    TIPO_ESTADO_CHOICES = [
        ('OK', 'Funcionando'),
        ('PF', 'ProximoFallo'),
        ('1F', 'Fallo'),
    ]
    comp_neg = models.ForeignKey(ComponenteNegocio, null=True, on_delete=models.SET_NULL)
    puesto_trabajo = models.CharField(max_length=50)
    responsable = models.ForeignKey(Personal, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField()
    fecha_fabricacion =  models.DateField()
    fecha_actual =  models.DateField(auto_now_add=True)
    tipo_sist = models.CharField(max_length=30, default="Sistema Operativo")
    estado = models.CharField(max_length=45, choices=TIPO_ESTADO_CHOICES, default='Funcionando', editable=True)
    items = models.ManyToManyField(Item)
    desc = models.TextField(default="Sin Observaciones")
    activo1 = models.BooleanField(blank=False, null=False, default=True, editable=True, help_text='Estado Lógico del Registro (Activo|Inactivo)', verbose_name='Activo')
    ip_add = models.GenericIPAddressField(protocol='IPv4', default="0.0.0.0")
        
    def _only_year(self):
        var1 = self.fecha_fabricacion.strftime('%Y')
        return var1
    fecha_fab_anual = property(_only_year)

    @property
    def expected_return(self):
        var = self.fecha_actual.year - self.fecha_fabricacion.year
        if var >= 5:
            i = "A Baja"
        else:
            i = "Activo"
        return i
    
    def __str__(self):
        return u'%s-%s' % (self.puesto_trabajo, self.fecha_fab_anual)

    class Meta:
        ordering = ('comp_neg', 'responsable')
        verbose_name_plural = 'Equipos'
        db_table = 'relacion_equipos_hardware'



   

