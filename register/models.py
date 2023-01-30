from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  urgente = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

# 1. IDENTIFICACIÓN DEL CASO
  municipio = models.CharField(max_length=50)
  parroquia = models.CharField(max_length=50)
  referido = models.CharField(max_length=50)
  ci_referido = models.IntegerField(null=True, blank=True)

  def __str__(self):
        txt1 = "{0}"
        return txt1.format(self.municipio)

  # 2. DATOS DE IDENTIFICACIÓN
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  ci = models.IntegerField(null=True, blank=True)
  fecha_n = models.DateField(null=True, blank=True)
  lugar_n = models.CharField(max_length=100)
  estado_civil = [
    ('S', 'Soltera'),
    ('C', 'Casada'),
    ('D', 'Divorciada'),
    ('V', 'Viuda')
  ]
  est_civil = models.CharField(max_length=1, choices=estado_civil, default='S')
  direccion = models.CharField(max_length=50)
  sabe_leer_escribir = models.BooleanField(default=True)
  ocupacion = models.CharField(max_length=100)

  def __str__(self):
        txt2 = "{0}"
        return txt2.format(self.nombre)

  # 3. DATOS FAMILIAR
  nombre_apellido_f = models.CharField(max_length=150)
  edad_f = models.IntegerField(null=True, blank=True)
  ci = models.IntegerField(null=True, blank=True)
  estado_civil_f = [
    ('S', 'Soltera'),
    ('C', 'Casada'),
    ('D', 'Divorciada'),
    ('V', 'Viuda')
  ]
  est_civil_f = models.CharField(max_length=1, choices=estado_civil_f, default='S')
  ocupacion_f = models.CharField(max_length=100)

  def __str__(self):
        txt = "{0}"
        return txt.format(self.nombre_apellido_f)

  # 4. CONDICIONES DE VIVIENDA
  casa = [
    ('P', 'Propia'),
    ('A', 'Alquilada'),
    ('P', 'Prestada')
  ]
  vivienda = models.CharField(max_length=1, choices=casa, default='P')
  parades = models.CharField(max_length=50)
  piso = models.CharField(max_length=50)
  techo = models.CharField(max_length=50)
  cuartos = models.IntegerField(null=True, blank=True)
  comedor = models.BooleanField(default=True)
  sala = models.BooleanField(default=True)
  cocina = models.BooleanField(default=True)
  servicio = [
    ('TV', 'TV'),
    ('LUZ', 'Luz'),
    ('AGUA', 'Agua'),
    ('ASEO', 'Aseo')
  ]
  servicios = models.CharField(max_length=4, choices=servicio, default=True)

  def __str__(self):
        txt3 = "Características de la Vivienda"
        return txt3
  
  # 5. SITUACIÓN SOCIO-ECONÓMICA
  sueldo = models.IntegerField(null=True, blank=True)
  subsidios = models.IntegerField(null=True, blank=True)
  becas_pen_jub = models.IntegerField(null=True, blank=True)
  ayudas_familiares = models.IntegerField(null=True, blank=True)
  otros = models.IntegerField(null=True, blank=True)
  total_ingresos = models.IntegerField(null=True, blank=True)
  vivienda = models.IntegerField(null=True, blank=True)
  servicios = models.IntegerField(null=True, blank=True)
  transporte = models.IntegerField(null=True, blank=True)
  medicinas = models.IntegerField(null=True, blank=True)
  total_egresos = models.IntegerField(null=True, blank=True)

  def __str__(self):
        txt4 = "Datos Económicos"
        return txt4

  # 6. ÁREA DE SALUD
  enf_padecidas = models.CharField(max_length=200)
  enf_actuales = models.CharField(max_length=200)
  medico_tratante = models.CharField(max_length=100)
  lugar = models.CharField(max_length=100)

  # 7. OBSERVACIONES
  observaciones = models.TextField(max_length=1000)