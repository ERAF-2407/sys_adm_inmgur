from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title + ' - ' + self.user.username


"""

  # 1. IDENTIFICACIÓN DEL CASO
  municipio = models.CharField(max_length=50)
  parroquia = models.CharField(max_length=50)
  referido = models.CharField(max_length=50)
  ci_referido = models.CharField(max_length=50)

  # 2. DATOS DE IDENTIFICACIÓN
  
  nombre = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  ci = models.IntegerField()
  fecha_nacimiento = models.DateTimeField(auto_now_add=True)
  lugar_nacimiento = models.CharField(max_length=50)
  estado_civil_soltera = models.BooleanField(default=False)
  estado_civil_casada = models.BooleanField(default=False)
  estado_civil_divorsiada = models.BooleanField(default=False)
  estado_civil_viuda = models.BooleanField(default=False)
  direccion = models.CharField(max_length=50)
  sabe_leer_escribir = models.BooleanField(default=False)
  ocupacion = models.CharField(max_length=50)

  # 3. GRUPO FAMILIAR
  nombre_apellido_familiar = models.CharField(max_length=50)
  edad_familiar = models.IntegerField()
  estado_civil_soltera_familiar = models.BooleanField(default=False)
  estado_civil_casada_familiar = models.BooleanField(default=False)
  estado_civil_divorsiada_familiar = models.BooleanField(default=False)
  estado_civil_viuda_familiar = models.BooleanField(default=False)
  ocupacion_familiar = models.CharField(max_length=50)

  # 4. CONDICIONES DE VIVIENDA
  propia = models.BooleanField(default=False)
  alquilada = models.BooleanField(default=False)
  prestada = models.BooleanField(default=False)
  parades = models.CharField(max_length=50)
  piso = models.CharField(max_length=50)
  techo = models.CharField(max_length=50)
  cuartos = models.CharField(max_length=50)
  comedor = models.CharField(max_length=50)
  sala = models.CharField(max_length=50)
  cocina = models.CharField(max_length=50)
  tv = models.BooleanField(default=False)
  luz = models.BooleanField(default=False)
  agua = models.BooleanField(default=False)
  aseo = models.BooleanField(default=False)
  
  # 5. SITUACIÓN SOCIO-ECONÓMICA
  suldo = models.IntegerField()
  subsidios = models.IntegerField()
  becas_pensiones_jubilaciones = models.IntegerField()
  ayudas_familiares = models.IntegerField()
  otros = models.IntegerField()
  total_ingresos = models.IntegerField()
  vivienda = models.IntegerField()
  servicios = models.IntegerField()
  transporte = models.IntegerField()
  medicinas = models.IntegerField()
  total_egresos = models.IntegerField()

  # 6. ÁREA DE SALUD
  enfermedades_padecidas = models.CharField(max_length=50)
  enfermedades_actuales = models.CharField(max_length=50)
  medico_tratante = models.CharField(max_length=50)
  lugar = models.CharField(max_length=50)

  # 7. OBSERVACIONES
  comentario = models.TextField(max_length=1000)

"""